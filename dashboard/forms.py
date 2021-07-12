from django import forms

from .models import Order

from .models import Subscription


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class OrderCreateForm(BaseForm, forms.ModelForm):
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

#     class Meta:
#         model = Order
#         fields = ['date', 'title' ]


# class OrderEditForm(BaseForm, forms.ModelForm):

#     class Meta:
#         model = Order
#         fields = ['date', 'title', 'discount', 'is_paid']

PAYMENT_CHOICES= [
    ('one month', 'one month'),
    ('two months', 'two months'),
    ('three months', 'three months'),
    ('four months', 'four months'),
    ('five months', 'five months'),
    ('six months', 'six months'),
    ]


class OrderForm(forms.ModelForm):
    firstname     = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    lastname     = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))
    company_name     = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Company Name'}))
    email    = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    address     = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}))
    product_one     = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Product Name'}))
    quantity_one     = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Quantity'}))
    product_two     = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Product Name'}))
    quantity_two     = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Quantity'}))
    product_three     = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Product Name'}))
    quantity_three     = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Quantity'}))
    product_four     = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Product Name'}))
    quantity_four     = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Quantity'}))
    total_price     = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Total Price '}))
    telephone     = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}))
    paymentplan     = forms.CharField(required=False, widget=forms.Select(choices=PAYMENT_CHOICES))
    

    class Meta:
        model = Order
        fields = (
            'firstname',
            'lastname',
            'company_name',
            'email',
            'address',
            'product_one',
            'product_two',
            'product_three',
            'product_four',
            'total_price',
            'telephone',
            'paymentplan'
            )


class SubscriptionForm(forms.ModelForm):
    email    = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = Subscription
        fields = (
            'email',
        )