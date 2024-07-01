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
        
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True  # Add is_staff for superuser
        user.save()
        return user

class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  # Add is_active field
    is_staff = models.BooleanField(default=False)  # Add is_staff field

    groups = models.ManyToManyField(
        Group,
        related_name='appuser_set',  # Add a unique related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='appuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='appuser_set',  # Add a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='appuser',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AppUserManager()

    def __str__(self):
        return self.username
