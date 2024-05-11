from django.shortcuts import render
from . models import Place
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    places = Place.objects.all()
    return render(request,'home/index.html',{'places':places})


@login_required
def home_detail(request,slug):
   
    places_detail = Place.objects.get(slug=slug)
    return render(request,'home/detail.html',{'place':places_detail})


def Payment(request, slug):
    payment = Place.objects.get(slug=slug)
    return render(request, 'home/payment.html', {'place': payment})
     

