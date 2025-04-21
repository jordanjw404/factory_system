from django import forms
from .models import Customer  # or your model name

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
#This part will make sure a valid email is entered in the form.
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'name@example.com',
            'class': 'form-control',
            'type': 'email',
        }),
        help_text="Enter a valid email address."
    )
