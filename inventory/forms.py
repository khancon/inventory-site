from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class UserForm(forms.Form):
    first_name = forms.CharField(
        label='First Name', 
        max_length=250,
        required=True
    )
    last_name = forms.CharField(
        label='Last Name', 
        max_length=250,
        required=True
    )
    street = forms.CharField(
        label='Street Address', 
        max_length=250,
        required=True
    )
    city = forms.CharField(
        label='City', 
        max_length=250,
        required=True
    )
    state = forms.CharField(
        label='State',
        max_length=2,
        required=True
    )
    zip_code = forms.IntegerField(
        label='Zip Code',
        max_value=99999,
        min_value=00000,
        required=True,
    )
    phone_number = forms.IntegerField(
        label="Phone Number (no dashes)",
        max_value=9999999999,
        min_value=0000000000,
        validators=[MinValueValidator(0000000000), MaxValueValidator(9999999999)],
        required=True,
    )

class ItemForm(forms.Form):
    item_name = forms.CharField(
        label="Item Name",
        max_length=250,
        required=True
    )
    price = forms.DecimalField(
        label="Price per unit",
        max_digits=7,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': '00000.00',
        }),
        required=True
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(),
        required=True
    )
    stock_quantity = forms.IntegerField(
        label="Quantity",
        required=True
    )
    photo = forms.ImageField(
        label='Image',
    )
