from urllib.parse import quote_plus
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.views.generic import DetailView, View
from .models import ProductCategory, Product, Subscription
from .forms import OrderForm, SubscriptionForm
from accounts import forms
from django import forms
from accounts.forms import CustomerRegForm
from accounts.models import CustomerReg
from hitcount.views import HitCountDetailView
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
from django.db.models import Sum
from .models import Order, OrderItem
from django.template.loader import render_to_string
from django.http import JsonResponse

from django.core.exceptions import ObjectDoesNotExist

import datetime

@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, "Product Added to cart " )
    return redirect("/dashboard/cart/cart-detail")

def cart_add_two(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, "Product Added to cart " )
    return redirect("/cart/cart-detail")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/dashboard/cart/cart-detail/")

def item_clear_two(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/cart/cart-detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/dashboard/cart/cart-detail")

def item_increment_two(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/cart/cart-detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/dashboard/cart/cart-detail")

def item_decrement_two(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/cart/cart-detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/dashboard/cart/cart-detail")

def cart_clear_two(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/cart/cart-detail")


@login_required
def cart_detail(request):
    cats = ProductCategory.objects.filter(parent=None)
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Subscription Successful" )
        return render(request, 'dashboard/cart-detail-two.html', { 'cats': cats, 'form': form})
    else:
        
        return render(request, 'dashboard/cart-detail-two.html', { 'cats': cats, 'form': form})

def cart_detail_two(request):
    cats = ProductCategory.objects.filter(parent=None)
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Subscription Successful" )
        return render(request, 'dashboard/cart-detail.html', { 'cats': cats, 'form': form})
    else:
        
        return render(request, 'dashboard/cart-detail.html', { 'cats': cats, 'form': form})

def checkout(request):
    cats = ProductCategory.objects.filter(parent=None)
    if request.method == 'POST':
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Order Submitted" )
            return render(request, 'dashboard/checkout.html',{'form':form, 'cats':cats})
        else:
            messages.error(request, "Order not successful")
            return render(request, 'dashboard/checkout.html',{'form':form, 'cats':cats})
    form = OrderForm(request.POST or None)
    return render(request, 'dashboard/checkout.html', {'form':form, 'cats': cats})

def checkout_two(request):
    cats = ProductCategory.objects.filter(parent=None)
    if request.method == 'POST':
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Order Submitted" )
            return render(request, 'dashboard/checkout2.html',{'form':form, 'cats':cats})
        else:
            messages.error(request, "Order not successful")
            return render(request, 'dashboard/checkout2.html',{'form':form, 'cats':cats})
    form = OrderForm(request.POST or None)
    return render(request, 'dashboard/checkout2.html', {'form':form, 'cats': cats})



# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('/cart/cart_detail')





def productList(request):
    cats = ProductCategory.objects.filter(parent=None)
    product_list = Product.objects.all()
    products = Product.objects.filter().order_by('-created_on')[0:20]
    best_sellers = Product.objects.filter().order_by('-created_on')[0:20]
    latest_products = Product.objects.filter().order_by('-created_on')[0:20]
    user_count = CustomerReg.objects.count()
    # order = Order.objects.all()[:10]
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Subscription Successful" )
        return redirect('/')
    else:
        return render(request, 'dashboard/index.html',{'product_list': product_list,'form': form, 'best_sellers':best_sellers, 'latest_products': latest_products ,'user_count': user_count,'products': products, 'cats': cats})
    

@login_required
def productList_two(request):
    cats = ProductCategory.objects.filter(parent=None)
    product_list = Product.objects.all()
    products = Product.objects.filter().order_by('-created_on')[0:20]
    user_count = CustomerReg.objects.count()
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Subscription Successful" )
        return redirect('/dashboard/home')
    else:
        return render(request, 'dashboard/index2.html',{'product_list': product_list,'user_count': user_count,'products': products,'form': form, 'cats': cats})
    

class ProductDetail(HitCountDetailView):
    model = Product
    template_name = 'dashboard/product_detail.html'
    context_object_name = 'product'
    form_class = SubscriptionForm
    slug = 'slug'
    count_hit = True
    
        
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context.update({
        'cats' : ProductCategory.objects.filter(parent=None),
        'user_count' : CustomerReg.objects.count(),
        'form' : SubscriptionForm(self.request.POST or None),
        
        })
        return context

    def post(self, request, *args, **kwargs):
        form = SubscriptionForm()
        if form.is_valid():
            form.save()
            self.object = self.get_object()
            context = super(SubscriptionForm, self).get_context_data(**kwargs)
            context['form'] = SubscriptionForm
            return self.render_to_response(context=context)

        else:
            self.object = self.get_object()
            context = super(ProductDetail, self).get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response( context=context)


class active_ProductDetail(HitCountDetailView):
    model = Product
    template_name = 'dashboard/product_detail2.html'
    context_object_name = 'product'
    form_class = SubscriptionForm
    slug = 'slug'
    count_hit = True
    
        
    def get_context_data(self, *args, **kwargs):
        context = super(active_ProductDetail, self).get_context_data(**kwargs)
        context.update({
        'cats' : ProductCategory.objects.filter(parent=None),
        'user_count' : CustomerReg.objects.count(),
        'form' : SubscriptionForm(self.request.POST or None),
        })
        return context

    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST or None)
        if form.is_valid():
            form.save()
            self.object = self.get_object()
            context = context = super(active_ProductDetail, self).get_context_data(**kwargs)
            context['form'] = SubscriptionForm
            return self.render_to_response(context=context)

        else:
            self.object = self.get_object()
            context = super(active_ProductDetail, self).get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response( context=context)



# def product_detail(request, slug):
#     cats = ProductCategory.objects.all()
#     product = get_object_or_404(Product, slug=slug)
#     product_image = quote_plus(product.image.url)
#     product_name = quote_plus(product.name)
#     user_count = CustomerReg.objects.count()
#     form = CustomerRegForm(request.POST or None)
#     context = {
#         "name": product.name,
#         "product": product,
#         "product_image": product_image,
#         "product_name": product_name,
#         "cats": cats,
#         "user_count": user_count,
#         "form":form
#     }
#     return render(request, "dashboard/product_detail.html", context) 
    

    
def product_category(request, category):
    category = Product.objects.filter(category_id=category) 
    cats = ProductCategory.objects.filter(parent=None)
    user_count = CustomerReg.objects.count()
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Subscription Successful" )
        return redirect('/dashbaord/home',{'category': category,'user_count': user_count, 'cats': cats, 'form':form})
    else:
        
        return render(request, 'dashboard/product_category.html',{'category': category,'user_count': user_count, 'cats': cats, 'form':form})
    
def product_category_two(request, category):
    category = Product.objects.filter(category_id=category) 
    cats = ProductCategory.objects.filter(parent=None)
    user_count = CustomerReg.objects.count()
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Subscription Successful" )
        return redirect('/dashbaord/home', {'category': category,'user_count': user_count, 'cats': cats, 'form':form})
    else:
        
        return render(request, 'dashboard/product_category2.html',{'category': category,'user_count': user_count, 'cats': cats, 'form':form})
    
    


def customer_email(request):
    form = CustomerEmailForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        form.save()
        return redirect('/dashbaord/successful')
    else:
        return render(request, 'dashboard/apply-leave.html',{'form':form})

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_item = OrderItem.objects.create(product=product)
    order_qs = Orders.objects.filter(user=request.user, complete=False)
    if order_qs.exists():
        order = order_qs[0]
    #check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.products.add(order_item)
    return redirect("dashboard: product_detail", slug=slug)

