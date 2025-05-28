from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

appname = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), #after logging out, user will be sent to login page
    path('account_details/', views.account_details, name='account_details'),
]