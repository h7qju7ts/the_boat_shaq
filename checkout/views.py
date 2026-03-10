from decimal import Decimal
from django.contrib import messages
from django.shortcuts import redirect, render
from boats.models import Boat
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def checkout(request):
    basket = request.session.get("basket", {})
    basket_items = []
    total = Decimal("0.00")

    if not basket:
        messages.info(request, "Your basket is empty")
        return redirect("basket:basket")

    for boat_id, quantity in basket.items():
        boat = Boat.objects.get(pk=boat_id)
        price = boat.price if boat.price else Decimal("0.00")
        subtotal = price * quantity
        total += subtotal

        basket_items.append({
            "boat": boat,
            "quantity": quantity,
            "subtotal": subtotal,
        }) 

    if request.method =="POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            messages.success(request, "Checkout complete! Your order has been placed.")
            request.session["basket"] = {}
            return redirect("boats:catalog")
    else:
        form = CheckoutForm()


    context = {
        "form": form,
        "basket_items": basket_items,
        "total": total,
    }                   
    return render(request, "checkout/checkout.html", context)
