from django.urls import path
from dashboard import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [

    # path('home/', views.index, name='home'), #view homepage
    path('product_category/<int:category>/', views.product_category, name='product_category'), #view category
    path('<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    # path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('', TemplateView.as_view(template_name='index.html', extra_context={
        "instagram_profile_name": "amd"
    })),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    ]
