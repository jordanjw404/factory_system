from django import forms
from .models import Order, OrderAttachment

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = OrderAttachment
        fields = ['file']
