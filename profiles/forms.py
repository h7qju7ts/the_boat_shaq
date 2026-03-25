from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "default_full_name",
            "default_email",
            "default_phone_number",
            "default_street_address1",
            "default_street_address2",
            "default_town_or_city",
            "default_county",
            "default_postcode",
            "default_country",
        ]


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["old_password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Current password",
            "autocomplete": "current-password",
        })

        self.fields["new_password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "New password",
            "autocomplete": "new-password",
        })

        self.fields["new_password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm new password",
            "autocomplete": "new-password",
        })