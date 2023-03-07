
from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id':'name', 'placeholder':'Your name', 'required':True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id':'email', 'placeholder':'Your email', 'required':True}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'id':'subject', 'placeholder':'Subject', 'required':True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id':'message', 'placeholder':'Message', 'required':True}),
        }