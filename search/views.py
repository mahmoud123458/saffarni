from django.shortcuts import render
from home.models import Place
from .models import Hotel
from .filters import HotelFilter
from django.contrib.auth.decorators import login_required

# Create your views here.

def search(request):
    hotels=Hotel.objects.all()
    myfilter=HotelFilter(request.GET,queryset=hotels)
    hotels=myfilter.qs
    return render(request,'search.html',{'hotels':hotels,'myfilter':myfilter})

@login_required
def book_hotel(request,slug):
   
    hotel_detail = Hotel.objects.get(slug=slug)
    
    return render(request,'bookHotel.html',{'hotel':hotel_detail})

def Payment_hotel(request, slug):
    payment = Hotel.objects.get(slug=slug)
    total_price = request.GET.get('total_price')

    return render(request, 'payment_hotel.html', {'hotel': payment,'total_price': total_price})
     