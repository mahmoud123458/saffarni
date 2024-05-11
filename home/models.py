from django.db import models
from django.utils.text import slugify
# Create your models here.
def image_upload(instance,filename):
    imagename,extenstion = filename.split(".")
    return "imagehome/%s.%s"%(instance.id,extenstion)


continent=[
    ('Asia','Asia'),
    ('Africa','Africa'),
    ('America','America'),
    ('Europe','Europe'),

]

period=[
    ('Days','Days'),
    ('Weeks','Weeks'),
    ('Months','Months'),
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
    
    slug=models.SlugField(blank=True,null=True)
    

    def save(self,*args, **kwargs):
        self.slug=slugify(self.city)
        super(Place,self).save(*args, **kwargs)


    def half_price(self):
        return self.price / 2
    
    
    def __str__(self):
        return self.city
    
