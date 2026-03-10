from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "county",
            "postcode",
            "country",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "full_name": "Enter your full name",
            "email": "Enter your email",
            "phone_number": "Enter your phone number",
            "street_address1": "House number and street name",
            "street_address2": "Apartment, suite, unit etc. (optional)",
            "town_or_city": "Town or City",
            "county": "County",
            "postcode": "Postcode",
            "country": "Country",
        }

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = placeholders.get(field_name, "")