from django.shortcuts import render

from .models import *


# Create your views here.

def master(request):
    return render(request,'master.html') 

def about(request):
    return render(request,'about.html')

def registration(request):
    return render(request,'registration.html')

def signup(request):

    error_msg = ''
    success_msg = ''

    if request.method == 'POST':
        name = request.POST['u_name']
        email = request.POST['u_email']
        address = request.POST['u_address']
        number = request.POST['u_number']
        password = request.POST['u_password']

        email_exist = Signup.objects.filter(u_email = email).exists()
        if not email_exist:
             
          signup = Signup(u_name = name, u_email = email, u_address = address, u_number = number, u_password = password)
          signup.save() 
          success_msg = 'you where registered'
        else:
            error_msg = 'Email Exists'   

 
     
    return render(request,'signup.html',{'error_message' : error_msg, 'succes_message' : success_msg} )

def login(request):

    msg = ''

    if request.method == 'POST':
        username = request.POST['u_email']
        password = request.POST['password']
 
             
        try :
                login = Signup.objects.get(u_email = username, password = password)
                
        except :
                msg = 'Invalid Username Or Password'

    return render(request,'login.html',{'error_msg' : msg,})

def contact(request):
    return render(request,'contact.html')

def complaint(request):
    return render(request,'complaint.html')

def home(request):
    return render(request,'home.html')

def help(request):
    return render(request,'help.html')




