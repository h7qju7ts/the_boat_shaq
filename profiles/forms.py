from django import forms
from .models import UserProfile

class UserProfileForm(forms. ModelForm):
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