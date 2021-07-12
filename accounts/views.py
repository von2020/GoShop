from django.shortcuts import render, redirect, HttpResponse
from accounts import forms
from accounts.forms import CustomerRegForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from dashboard.models import ProductCategory, Order
from .models import CustomerReg
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
# def login(request):
#     return render(request, 'dashboard/accounts.html')

def register(request):
    cats = ProductCategory.objects.filter(parent=None)
    if request.method == 'POST':
        form = CustomerRegForm(request.POST , request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful." )
            return redirect('/')
        else:
            messages.error(request, "Sign Up not successful")
            return render(request, 'dashboard/register.html',{'form':form, 'cats':cats})
        
    else: 
        form = CustomerRegForm()   
        return render(request, 'dashboard/register.html',{'form':form, 'cats': cats})


def register_two(request):

    if request.method == 'POST':
        form = CustomerRegForm_two(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign Up Successful. A Confirmation Message has been sent to your Email Address. Click on the link in your email address to continue Registration " )
            return redirect('/')
        else:
            return render(request, 'dashboard/register_two.html',{'form':form})
        messages.error(request, "Sign Up not successful")
    else: 
        form = CustomerRegForm_two()   
        return render(request, 'dashboard/register_two.html',{'form':form})


def loginPage(request):
    cats = ProductCategory.objects.filter(parent=None)
    if request.method == 'POST':
        # form = LoginForm(data=request.POST)
    
        # if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
        
            if user is not None:
                # if user.is_active:
                    login(request, user)
                    messages.success(request, "You are now logged in " )
                    return redirect('/dashboard/home', {'cats': cats})
            else:
                messages.error(request, "You are not a registered customer, CLICK ON MY ACCOUNT TO SIGN UP")
                return render(request, 'dashboard/index.html', {'cats': cats})
            
    else:
        form = LoginForm()
        return render(request, 'dashboard/accounts.html', {'form':form, 'cats': cats})

@login_required
def profile(request):
    cats = ProductCategory.objects.filter(parent=None)
    orders = Order.objects.all()
    customers = CustomerReg.objects.all()
    return render(request, 'dashboard/profile.html',{'cats':cats, 'orders':orders, 'customers': customers})

def logoutUser(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('/')


def success(request, uid):
    template = render_to_string("dashboard/email_template.html")

    email = EmailMessage(
        'Thanks For Registring With Us',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email]
    )
    email.fail_silently = False
    email.send()
    messages.success(request, "Registration Successful." )
    return redirect('/')