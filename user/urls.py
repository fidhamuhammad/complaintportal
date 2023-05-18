from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('master', views.master, name='master'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='registration'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('contact',views.contact, name='contact'),
    path('complaint',views.complaint, name='complaint'),
    path('home',views.home, name='home'),
    path('help',views.help, name='help')

]