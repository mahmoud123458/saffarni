from django.db import models

# Create your models here.
def image_upload2(instance,filename):
    imagename,extenstion = filename.split(".")
    return "imagehotel/%s.%s"%(instance.id,extenstion)

features=[
    (' Wi-Fi',' Wi-Fi'),
    ('parking','parking'),
    ('swimming pool','swimming pool'),
    ('garden','garden'), 
    ('The mosque','The mosque'),
    (' Air conditioning',' Air conditioning'),
    (' cafe',' cafe'),
    ('Barber/beauty salon','Barber/beauty salon'),
    ('Luggage storage','Luggage storage'),
    ('Restaurant','Restaurant'),
   

]
class Hotel(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField( max_length=50)
    country = models.CharField(max_length=30)
    image = models.ImageField(upload_to=image_upload2)
    features1=models.CharField( max_length=50,choices=features)  
    features2=models.CharField( max_length=50,choices=features)
    features3=models.CharField( max_length=50,choices=features)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
   
