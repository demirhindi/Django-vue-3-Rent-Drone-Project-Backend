from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.

class DroneCategory(models.Model):
    title = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(blank=True)    
    created_at = models.DateField(auto_now_add=True)    

    def __str__(self):
        return self.title

class Drones(models.Model):
    categories = models.ForeignKey(DroneCategory,related_name='drones',on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    slug = models.SlugField(blank=True)
    brand = models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to="drones",blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=0,blank=True, null=True)
    description=models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return self.title


class Features(models.Model):
    drone=models.ForeignKey(Drones,related_name='feature',on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True)
    description=models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return self.title

class Orders(models.Model):
    user=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    drone=models.ForeignKey(Drones,related_name='drone',on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True)
    adress=models.TextField(max_length=1000,blank=True)
    quantity=models.IntegerField(default=0,blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)  
    end_date = models.DateField(blank=True, null=True)  
    created_at = models.DateField(auto_now_add=True)   
    status=models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.title


def pre_save_dronecategory(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_dronecategory,sender=DroneCategory)

def pre_save_drones(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_drones,sender=Drones)

