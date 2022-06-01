from django.contrib.auth import views as auth_views
#from django.conf.urls import url
from django.urls import re_path
from .import views
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from django.views.generic import TemplateView
app_name='user'

urlpatterns = [
    re_path('login/',auth_views.LoginView.as_view(template_name="user/login.html"),name='login'),
    re_path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    re_path('signup/',views.SignUp.as_view(),name='signup'),
    re_path('',views.base),
    re_path('',views.dashboard.as_view(),name='dashboard')

]