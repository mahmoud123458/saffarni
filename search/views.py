from django.shortcuts import render
from home.models import Place
from .models import Hotel
from .filters import HotelFilter
# Create your views here.

def search(request):
    hotels=Hotel.objects.all()
    myfilter=HotelFilter(request.GET,queryset=hotels)
    hotels=myfilter.qs
    return render(request,'search.html',{'hotels':hotels,'myfilter':myfilter})

def Payment_hotel(request, slug):
    payment = Place.objects.get(slug=slug)
    return render(request, 'payment_hotel.html', {'hotel': payment})
     