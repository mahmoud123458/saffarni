from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from djstripe.models import StripeModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from accounts.models import AppUser

from search.models import Hotel
# Create your models here.
def image_upload(instance,filename):
    imagename,extenstion = filename.split(".")
    return "imagehome/%s.%s"%(instance.id,extenstion)


continent=[
    ('أسيا','أسيا'),
    ('أفريقيا','أفريقيا'),
    ('أمريكا','أمريكا'),
    ('أوروبا','أوروبا'),

]

period=[
    ('Days','Days'),
    ('Weeks','Weeks'),
    ('Months','Months'),
]

source=[
    ('Egypt','Egypt'),
    ('Cairo International Airport','Cairo International Airport'),
    
]

flight_class=[
    ('FirstClass','FirstClass'),
    ('BusnissClass','BusnissClass'),
    ('PremiumClass','PremiumClass'),
    ('EconomyClass','EconomyClass'),

]

class Place(models.Model):
    city = models.CharField(max_length=30)
    continent = models.CharField(max_length=30,choices=continent)
    country = models.CharField(max_length=30)
    image = models.ImageField(upload_to=image_upload)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount=models.DecimalField(max_digits=8, decimal_places=2)
    period=models.CharField(max_length=30,choices=period)
    duration=models.IntegerField(null=True,blank=True)
    source=models.CharField( max_length=50,choices=source) 
    date=models.DateField(auto_now=False, auto_now_add=False)
    flight_class=models.CharField(max_length=50,choices=flight_class)

    
    slug=models.SlugField(blank=True,null=True)
    

    def save(self,*args, **kwargs):
        self.slug=slugify(self.city)
        super(Place,self).save(*args, **kwargs) 
        



    def half_price(self):
        return self.price / 2
    
    
    def __str__(self):
        return self.city
    

class Continent(models.Model):
    name=models.CharField(max_length=50,choices=continent)
    photo=models.ImageField(upload_to=image_upload)
        
    def __str__(self):
        return self.name
    
class UserPayment(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	payment_bool = models.BooleanField(default=False)
	stripe_checkout_id = models.CharField(max_length=500)


@receiver(post_save, sender=AppUser)
def create_user_payment(sender, instance, created, **kwargs):
	if created:
		UserPayment.objects.create(app_user=instance)