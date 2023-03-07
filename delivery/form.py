from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Delivery


class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        exclude = ["id"]
        fields = ['name', 'email', 'address', 'phone', 'measurements', 'items']

    name = forms.CharField(label="Enter your full Name", widget=forms.TextInput(
        attrs={'placeholder': 'Full name please', 'class': 'form-control'}))
    email = forms.CharField(label="Enter your Email address", widget=forms.EmailInput(
        attrs={'placeholder': 'Enter a valid email address', 'class': 'form-control'}))
    address = forms.CharField(label="Enter Your delivery address", widget=forms.TextInput(
        attrs={'placeholder': 'Delivery address', 'class': 'form-control'}))
    phone = forms.CharField(label="Enter your phone number", widget=forms.NumberInput(
        attrs={'placeholder': 'A valid phone number', 'class': 'form-control'}))
    items = forms.CharField(label="Items being ordered", widget=forms.TextInput(
        attrs={'placeholder': 'Will be filled automatically', 'class': 'form-control'}))
    measurements = forms.CharField(widget=CKEditorWidget(
        attrs={'class': 'form-control', 'rows': '3'}))
