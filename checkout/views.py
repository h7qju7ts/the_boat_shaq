from decimal import Decimal

from django.contrib import messages
from django.shortcuts import redirect, render
from boats.models import Boat
from profiles.models import UserProfile
from django.shortcuts import get_object_or_404

from .forms import CheckoutForm
from .models import OrderLineItem


def checkout(request):
    basket = request.session.get("basket", {})
    basket_items = []
    total = Decimal("0.00")

    if not basket:
        messages.info(request, "Your basket is empty.")
        return redirect("basket:basket")

    for boat_id, quantity in basket.items():
        boat = get_object_or_404(Boat, pk=boat_id)
        price = boat.price if boat.price else Decimal("0.00")
        subtotal = price * quantity
        total += subtotal

        basket_items.append({
            "boat": boat,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            if request.user.is_authenticated:
                profile, created = UserProfile.objects.get_or_create(user=request.user)
                order.user_profile = profile

            order.save()

            for item in basket_items:
                OrderLineItem.objects.create(
                    order=order,
                    boat=item["boat"],
                    quantity=item["quantity"],
                )

            order.update_total()
            request.session["basket"] = {}
            messages.success(request, "Order placed successfully.")
            return redirect("profiles:profile")

    else:
        form = CheckoutForm()

    context = {
        "form": form,
        "basket_items": basket_items,
        "total": total
    }        

    return render(request, "checkout/checkout.html", context)