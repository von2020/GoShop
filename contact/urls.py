from django.urls import path
from contact import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [

    path('emailsent/',views.emailsent, name='emailsent'),
    path('contact-us/',views.contact, name='contact'),
    # path('like/', views.like_post, name='like-post'),
    
    ]
