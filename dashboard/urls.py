from django.urls import path


from dashboard import views

from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [

    path('home/', views.productList_two, name='homeActive'), #view logged inhomepage
    path('product_category/<int:category>/', views.product_category_two, name='product_category'), #view category
    # path('<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('<slug:slug>/', views.active_ProductDetail.as_view(), name='activeUser_productDetail'),
    # path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('', TemplateView.as_view(template_name='index.html', extra_context={
        "instagram_profile_name": "amd"
    })),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    # path('<slug:slug>/', views.add_to_cart, name='add-to-cart'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    

    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    

    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    

    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    

    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    

    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

    # path('cart/checkout/', views.checkout, name='checkout'),
    
    path('cart/checkout/', views.checkout_two, name='checkout'),
    

    ]
