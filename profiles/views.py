from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import UserProfile
from .forms import UserProfileForm, CustomPasswordChangeForm


@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if created and not profile.default_email:
        profile.default_email = request.user.email
        profile.default_full_name = request.user.get_full_name()
        profile.save()

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profiles:profile")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all().order_by("-date")

    context = {
        "profile": profile,
        "form": form,
        "orders": orders,
    }
    return render(request, "profiles/profile.html", context)


class CustomPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = "account/password_change.html"
    success_url = reverse_lazy("profiles:password_change_done")
    success_message = "Your password was updated successfully."