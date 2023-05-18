from django.urls import path
from . import views

app_name = 'cp_admin'

urlpatterns = [
    path('admin_master', views.admin_master, name='admin_master'),
    path('profile', views.profile, name='profile')



]