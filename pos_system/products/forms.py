from django import forms
from .models import Product
from categories.models import Category  # Ensure correct import


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=None,  # Prevents empty selection
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'cost_price', 'price', 'stock', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cost Price'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock Quantity'}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=[('active', 'Active'), ('inactive', 'Inactive')]),
        }

    def clean_sku(self):
        sku = self.cleaned_data.get('sku')
        if Product.objects.filter(sku=sku).exists():
            raise forms.ValidationError(
                "This SKU is already in use. Please enter a unique SKU.")
        return sku
