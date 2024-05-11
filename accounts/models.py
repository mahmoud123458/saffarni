from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class City(models.Model):
    name= models.CharField( max_length=50)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    city= models.ForeignKey('City', on_delete=models.CASCADE,blank=True,null=True)
    phone_number=models.CharField(max_length=15)
    image=models.ImageField(upload_to="profile/",null=True,blank=True)
    address = models.CharField(max_length=100)  # Add the address field



    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

