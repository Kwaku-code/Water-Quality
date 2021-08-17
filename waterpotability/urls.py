from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('SignUp/', views.SignUp.as_view(), name='signup'),
    path('Database/', views.Database.as_view(), name='database'),
]
