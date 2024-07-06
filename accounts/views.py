from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login as auth_login
from django.urls import reverse
from django.db import IntegrityError

from .forms import SignupForm,UserForm,ProfileForm,LoginForm
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
        form = SignupForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            image = form.cleaned_data.get('image')  # Get photo from cleaned data

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
            
            if user and user.is_superuser:
                messages.warning(request, 'Admin users cannot log in here.')
                return redirect('/admin/')
            
            login(request, user)
            return redirect(reverse('accounts:profile'))

    else:
        form = SignupForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})



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


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_superuser:
                    messages.warning(request, 'المسؤولون لا يمكنهم تسجيل الدخول هنا. يرجى استخدام لوحة المسؤول.')
                    return redirect('/admin/login/?next=/admin/')
                else:
                    auth_login(request, user)
                    next_url = request.POST.get('next', reverse('home'))
                    return redirect(next_url)
            else:
                messages.error(request, 'اسم المستخدم وكلمة المرور غير متطابقين. يرجى المحاولة مرة أخرى.')
    else:
        form = LoginForm()
    
    context = {
        'form': form,
        'next': request.GET.get('next', '')
    }
    return render(request, 'registration/login.html', context)