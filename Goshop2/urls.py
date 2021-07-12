"""goshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from dashboard import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.productList, name='home'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product_category/<int:category>/', views.product_category, name='product_category'),

    path('cart/add/<int:id>/', views.cart_add_two, name='cart_add_two'),
    path('cart/item_clear/<int:id>/', views.item_clear_two, name='item_clear_two'),
    path('cart/item_increment/<int:id>/', views.item_increment_two, name='item_increment_two'),
    path('cart/item_decrement/<int:id>/', views.item_decrement_two, name='item_decrement_two'),
    path('cart/cart_clear/', views.cart_clear_two, name='cart_clear_two'),
    path('cart/cart-detail/',views.cart_detail_two, name='cart_detail_two'),
    path('cart/checkout/', views.checkout, name='checkout'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
