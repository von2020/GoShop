from urllib.parse import quote_plus
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from .models import ProductCategory, Product
from accounts import forms
from django import forms
from accounts.forms import CustomerRegForm
from accounts.models import CustomerReg
from hitcount.views import HitCountDetailView





def productList(request):
    cats = ProductCategory.objects.all()
    product_list = Product.objects.all()
    products = Product.objects.filter().order_by('-created_on')[0:20]
    user_count = CustomerReg.objects.count()
    form = CustomerRegForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return render(request, 'dashboard/index.html',{'product_list': product_list,'user_count': user_count,'products': products, 'cats': cats, 'form': form})

class ProductDetail(HitCountDetailView):
    model = Product
    template_name = 'dashboard/product_detail.html'
    context_object_name = 'product'
    form_class = CustomerRegForm
    slug = 'slug'
    count_hit = True
    
        
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context.update({
        'cats' : ProductCategory.objects.all(),
        'user_count' : CustomerReg.objects.count(),
        'form' : CustomerRegForm(self.request.POST or None),
        })
        return context

    def post(self, request, *args, **kwargs):
        form = CustomerRegForm(request.POST or None)
        if form.is_valid():
            form.save()
            self.object = self.get_object()
            context = context = super(ProductDetail, self).get_context_data(**kwargs)
            context['form'] = CustomerRegForm
            return self.render_to_response(context=context)

        else:
            self.object = self.get_object()
            context = super(ProductDetail, self).get_context_data(**kwargs)
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
    cats = ProductCategory.objects.all()
    user_count = CustomerReg.objects.count()
    form = CustomerRegForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/dashbaord/emailsent')
    else:
        return render(request, 'dashboard/product_category.html',{'category': category,'user_count': user_count, 'cats': cats, 'form':form})
    


def customer_email(request):
    form = CustomerEmailForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        form.save()
        return redirect('/dashbaord/successful')
    else:
        return render(request, 'dashboard/apply-leave.html',{'form':form})
