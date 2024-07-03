from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.db import IntegrityError

from .forms import SignupForm,UserForm,ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import SignupForm, UserForm, ProfileForm
from .models import Profile

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            try:
                profile = Profile.objects.create(user=user, city=city, phone_number=phone_number)
            except IntegrityError:
                profile = Profile.objects.get(user=user)
                profile.city = city
                profile.phone_number = phone_number
                profile.save()

            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            
            # Check if the user is an admin (superuser)
            if user and user.is_superuser:
                # If admin, show a message and redirect
                messages.warning(request, 'Admin users cannot log in here.')
                return redirect('/admin/')
            
            # If not admin, log in the user and redirect to profile
            login(request, user)
            return redirect(reverse('accounts:profile'))

    else:
        form = SignupForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})



def profile_edit(request):
    profile=Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})