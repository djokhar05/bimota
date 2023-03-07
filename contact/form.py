from django import forms
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.Form):
    name = forms.CharField(label="Enter your name", min_length=5, widget=forms.TextInput(
        attrs={'placeholder': 'Full name please', 'class': 'form-control'}))
    email = forms.CharField(label="Enter your Email address", widget=forms.EmailInput(
        attrs={'placeholder': 'Enter a valid email address', 'class': 'form-control'}))
    subject = forms.CharField(label="Enter a subject for your message", widget=forms.TextInput(
        attrs={'placeholder': 'Message Subject', 'class': 'form-control'}))
    phone = forms.CharField(label="Enter your phone number", widget=forms.NumberInput(
        attrs={'placeholder': 'A valid phone number', 'class': 'form-control'}))
    # message = forms.CharField(label="Enter your message", widget=forms.Textarea(
    #     attrs={'placeholder': 'Please be detailed as possible', 'class': 'form-control', 'rows': '3'}))

    message = forms.CharField(widget=CKEditorWidget(
        attrs={'class': 'form-control', 'rows': '3'}))

    def send_email(self):
        pass
