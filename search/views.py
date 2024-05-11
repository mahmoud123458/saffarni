from django.shortcuts import render
from .models import Hotel
from .filters import HotelFilter
# Create your views here.

def search(request):
    hotels=Hotel.objects.all()
    myfilter=HotelFilter(request.GET,queryset=hotels)
    hotels=myfilter.qs
    return render(request,'search.html',{'hotels':hotels,'myfilter':myfilter})