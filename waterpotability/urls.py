from django.urls import path

# from django.contrib.auth import views as auth_views
from . import views
# app_name = 'waterpotability'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('SignUp/', views.SignUp.as_view(), name='signup'),
    path('Database/', views.Database.as_view(), name='database'),
]
