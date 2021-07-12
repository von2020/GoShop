from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import *
from .models import *
from django.utils import timezone
from dashboard.models import *

# Create your views here.



    # if request.user.is_authenticated:
    #     customer = request.user.email
    #     order= Orders.objects.get(customer=customer, complete=False)
    #     items = order.orderitem__set.all()
    # else:
    #     items = []

    # context = {'items':items}
    # return render(request, 'dashboard/cart.html', context)
    
        







        