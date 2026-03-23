from django import forms
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm


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
            "default_country"
        ]


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["oldpassword"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Current Password",
            "autocomplete": "current-password",
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "New Password",
            "autocomplete": "new-password",
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "New Password (again)",
            "autocomplete": "new-password",
        })