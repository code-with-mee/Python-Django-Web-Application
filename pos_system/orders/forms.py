from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_amount', 'payment_status']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Amount'}),
            'payment_status': forms.Select(attrs={'class': 'form-control'}),
        }
