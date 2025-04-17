from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class AttachmentForm(forms.Form):
    file = forms.FileField(required=False)  # No widget override here
