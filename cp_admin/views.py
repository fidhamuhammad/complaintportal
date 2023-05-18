from django.shortcuts import render
 

# Create your views here.

def admin_master(request):
    return render(request,'admin_master.html')

def profile(request):
    return render(request,'profile.html')


