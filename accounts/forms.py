from django import forms
from accounts.models import CustomerReg
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from contact.models import Message
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm

User = get_user_model()

class CustomerRegForm(UserCreationForm):
    firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Firstname'}))
    lastname  = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Lastname'}))
    email     = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    employment_status = forms.BooleanField(required=False,initial=False,label='Employment ')
    salary = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Salary'}))
    work_address  = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Work Address'}))
    # date_sent = forms.CharField(required=True, widget=forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Date Sent'}))
    phone_number = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}))
    bank_statement = forms.FileField(required=False, widget=forms.FileInput(attrs={'class':'form-control', 'placeholder': 'bank statement','help_text':'max. 42 megabytes'}))
    government_id = forms.FileField(required=False, widget=forms.FileInput(attrs={'class':'form-control', 'placeholder': 'government id','help_text':'max. 42 megabytes'}))
    work_id = forms.FileField(required=False, widget=forms.FileInput(attrs={'class':'form-control', 'placeholder': 'work id','help_text':'max. 42 megabytes'}))
    # password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
    # password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = (
            'firstname',
            'lastname',
            'email',
            'employment_status',
            'salary',
            'work_address',
            # 'date_sent',
            'phone_number',
            'bank_statement',
            'government_id',
            'work_id',
            'password1',
            'password2'
            )

    def save(self, commit=True):
        user = super(CustomerRegForm, self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.employment_status = self.cleaned_data['employment_status']
        user.salary = self.cleaned_data['salary']
        user.work_address = self.cleaned_data['work_address']
        user.phone_number = self.cleaned_data['phone_number']
        user.bank_statement = self.cleaned_data['bank_statement']
        user.government_id = self.cleaned_data['government_id']
        user.work_id = self.cleaned_data['work_id']
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        # if password1 and password2 and password1 != password2:
        #     raise forms.ValidationError(
        #         self.error_messages['password_mismatch'],
        #         code='password_mismatch',
        #     )
        # return password2
        # def _post_clean(self):
        #     super()._post_clean()
            # Validate the password after self.instance is updated with form data
            # by super().
            # password = self.cleaned_data.get('password2')
            # if password:
            #     try:
            #         password_validation.validate_password(password, self.instance)
            #     except forms.ValidationError as error:
            #             self.add_error('password2', error)


        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    email     = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'email'}))
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
    

    class Meta:
        model = User
        fields = (
            'email',
			'password1'
            )

    def save(self, commit=False):
        user = super(LoginForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        if commit:
            user.set_password(user.password)
            user.save()
            return user





class MessageForm(forms.ModelForm):
    name     = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}))
    email    = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    message  = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Message'}))

    class Meta:
        model = Message
        fields = (
            'name',
            'email',
            'message',
            )



class ResetPasswordForm(PasswordResetForm):
	password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Oya tell me your Password'}))
	# class Meta:
	# 	model = User
	# 	fields = (
	# 		'password1'
	# 		)
    #         def save(self, commit=True):
    #             user = super(ResetPasswordForm, self).save(commit=False)
	#             user.password1 = self.cleaned_data['password1']
			
	#         if commit:
	# 	        user.save()

	#         return user

    