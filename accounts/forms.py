from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,City


class SignupForm(UserCreationForm):
    city = forms.ModelChoiceField(queryset=City.objects.all())
    # address = forms.CharField(max_length=100)
    phone_number=forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'city','phone_number']


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]


class ProfileForm(forms.ModelForm):
     # Add address field to the profile edit form

    class Meta:
        model = Profile
        fields = ['city', 'phone_number', 'image']