from django import forms
from accounts.models import CustomerReg
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from contact.models import ContactUs

User = get_user_model()

class CustomerRegForm(forms.ModelForm):
    firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Firstname'}))
    lastname  = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Lastname'}))
    email     = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = (
            'firstname',
            'lastname',
            'email'
            )

    def save(self, commit=True):
        user = super(CustomerRegForm, self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user

class ContactUsForm(forms.ModelForm):
    name     = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}))
    email    = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    message  = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Message'}))

    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'message',
            )