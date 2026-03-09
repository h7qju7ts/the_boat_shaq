from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.decorators.http import require_POST
from boats.models import Boat


@require_POST
def add_to_basket(request, boat_id):
    boat = get_object_or_404(Boat, pk=boat_id)

    basket = request.session.get("basket", {})

    boat_id_str = str(boat_id)
    basket[boat_id_str] = basket.get(boat_id_str, 0) + 1

    request.session["basket"] = basket

    messages.success(request, f"{boat.name} added to your basket.")

    redirect_url = request.POST.get("redirect_url")
    return redirect(redirect_url or "boats:catalog")


@require_POST
def decrease_basket(request, boat_id):
    basket = request.session.get("basket", {})
    boat_id = str(boat_id)

    if boat_id in basket:
        basket[boat_id] -= 1
        if basket[boat_id] <= 0:
            del basket[boat_id]

    request.session["basket"] = basket
    return redirect("basket:basket")


@require_POST
def remove_from_basket(request, boat_id):
    basket = request.session.get("basket", {})
    boat_id = str(boat_id)

    if boat_id in basket:
        del basket[boat_id]

    request.session["basket"] = basket
    return redirect("basket:basket")


def view_basket(request):
    basket = request.session.get("basket", {})
    basket_items = []
    total = 0

    for boat_id, quantity in basket.items():
        boat = get_object_or_404(Boat, pk=boat_id)
        subtotal = (boat.price or 0) * quantity
        total += subtotal

        basket_items.append({
            "boat": boat,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    context = {
        "basket_items": basket_items,
        "total": total,
    }

    return render(request, "basket/basket.html", context)


@require_POST
def clear_basket(request):
    request.session["basket"] = {}
    return redirect("basket:basket")