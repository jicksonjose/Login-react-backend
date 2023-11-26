from django.db import models

# Create your models here.

class UserModel(models.Model):
    name=models.CharField(max_length=100, default="")
    phone=models.IntegerField()
    email=models.EmailField(max_length=100,default="")
    password=models.CharField(max_length=100,default="")
