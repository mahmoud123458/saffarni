from django.shortcuts import render

from search.models import Hotel
from . models import Place
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
def home(request):
    places = Place.objects.all()
    return render(request,'home/index.html',{'places':places})


@login_required
def home_detail(request,slug):
   
    places_detail = Place.objects.get(slug=slug)
    return render(request,'home/detail.html',{'place':places_detail})

from django.shortcuts import render
from search.models import Hotel
from .models import Place
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def Payment(request, slug):
    if request.method == 'POST':
        # Process the form data
        place_slug = slug
        total_price = request.POST.get('total_price')

        # Save the total price to the database
        payment = Place.objects.create(place_slug=place_slug, total_price=total_price)

        # Redirect to a success page or wherever you need to go
        return HttpResponseRedirect(reverse('success.html'))
    else:
        payment = Hotel.objects.get(slug=slug)
        return render(request, 'home/payment.html', {'place': payment})


     


def search_flights(request):
    if request.method == 'POST':
        # Process the form data
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        flight_class = request.POST.get('class')

        # Filter places based on the provided search parameters
        places = Place.objects.all()

        if destination:
            places = places.filter(country=destination)

        # Redirect to the 'shop' page with the filtered places
        return render(request, 'shop.html', {'places': places})
    else:
        # If the request is not POST, render the search form template
        return render(request, 'home/index.html')

def success(request):
        return render(request,'home/success.html',{})
