from django.urls import path
from blog import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [

    # path('all-posts/', views.blog, name='blog'), #view blogpage
    path('category/<int:category>/', views.category, name='category'), #view category
    path('all-posts/', views.postList, name='bloghome'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    # url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount2')),
    
    ] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
