from django import forms


class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your full name",
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email adress",
        })
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your phone number",
        })
    )
    street_address1 = forms.CharField(
        max_length=255,
        label="Street AdDress 1",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "House number and street name",
        })
    )
    street_address2 = forms.CharField(
        max_length=255,
        required=False,
        label="Street Address 2",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Apartment, suite, unit, etc... (optional)",
        })
    )
    town_or_city = forms.CharField(
        max_length=100,
        label="Town/City",
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    county = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    postcode = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
