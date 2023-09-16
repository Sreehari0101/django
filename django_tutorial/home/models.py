from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class department(models.Model):
    dep_name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.dep_name

class users(models.Model) :
    user_name=models.CharField(max_length=255)
    user_class=models.CharField(max_length=100)
    dep_name=models.ForeignKey(department,on_delete=models.CASCADE)

class login(models.Model):
  user_name=models.CharField(max_length=100)  
  login_password=models.CharField(max_length=255)


    
class Leave_apply(models.Model):
    std_id=models.IntegerField()
    leave_type=models.CharField(max_length=50)
    reason=models.TextField(max_length=50)
    on_date=models.DateTimeField(auto_now_add=True)

class Leave_request(models.Model):
    std_id=models.IntegerField()
    is_approved = models.BooleanField('approved',default=False)
    is_rejected = models.BooleanField('rejected',default=False)


   


    
    










   
    
  

    


