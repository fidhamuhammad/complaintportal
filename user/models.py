from django.db import models

# Create your models here.

class Signup(models.Model):
    u_name = models.CharField(max_length = 50)
    u_email = models.CharField(max_length = 50)
    u_number = models.CharField(max_length = 50) 
    u_address = models.CharField(max_length= 50)
    u_password = models.CharField(max_length=50)

     
    class Meta :
        db_table = 'reg_tb'
