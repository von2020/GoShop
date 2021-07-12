from django.urls import path
from accounts import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_view
from accounts.forms import LoginForm

urlpatterns = [


path('login/', views.loginPage, name='login'),
path('logout/', views.logoutUser, name='logout'),
path('register/', views.register, name='register'),
path('profile/', views.profile, name='profile'),
path('success/', views.success, name='success'),
path('reset_password/', auth_view.PasswordResetView.as_view(template_name="dashboard/reset-password.html"), name='reset_password'),
path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name="dashboard/reset-password-sent.html"), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="dashboard/reset-password-confirm.html"), name='password_reset_confirm'),
path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="dashboard/reset-password-complete.html"), name='password_reset_complete'),

# path('login/', auth_view.LoginView.as_view(template_name='dashboard/accounts.html', authentication_form=LoginForm)),

]