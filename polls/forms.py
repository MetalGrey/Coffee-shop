from django import forms
from .models import News, Order

class EmailForm(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ['adress']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email', 'address1', 'address2', 'city', 'prefecture', 'zip_code', 'fast_delivery']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'address1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 1'}),
            'address2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 2'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'prefecture': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prefecture'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'fast_delivery': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }