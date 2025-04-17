from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name',
            'contact_name',
            'email',
            'phone_number',
            'mobile',
            'address_1',
            'address_2',
            'city',
            'postcode',
            'notes'
        ]
