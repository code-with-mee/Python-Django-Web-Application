from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'  # Automatically includes all fields from the Supplier model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Supplier Address', 'rows': 3}),
        }
