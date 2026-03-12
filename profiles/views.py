from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    orders = profile.orders.all().order_by("-date")

    context = {
        "profile": profile,
        "orders": orders,
    }
    return render(request, "profiles/profile.html", context)