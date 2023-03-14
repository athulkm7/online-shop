from django.db import models

class customer(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Contactnumber = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="profile",null=True,blank=True)
class category(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Discription=models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
class proddetails(models.Model):
    price = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField()
    Desc = models.CharField(max_length=100, null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)






