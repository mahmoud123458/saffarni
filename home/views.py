from django.shortcuts import render

from search.models import Hotel
from . models import Place,Continent
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def home(request):
    continent = request.GET.get('continent')
    
    places = Place.objects.all()
    countries = Place.objects.values('country').distinct() 
    continents = Continent.objects.all()
    
    if continent:
        places = places.filter(continent=continent)
        return render(request, 'shop.html', {'places': places})
    else:
        return render(request, 'home/index.html', {'places': places, 'countries': countries, 'continents': continents})


@login_required
def home_detail(request,slug):
   
    places_detail = Place.objects.get(slug=slug)
    
    return render(request,'home/detail.html',{'place':places_detail})




from django.conf import settings
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def Payment(request, slug):
    place = Place.objects.get(slug=slug)
    total_price = request.GET.get('total_price')

    if request.method == 'POST':
        try:
            # Create a Stripe charge
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency='usd',
                description='Example charge',
                source=request.POST['stripeToken']
            )
            return render(request, 'home/success.html')
        except stripe.error.CardError as e:
            return render(request, 'home/payment_error.html', {'error': e})
    else:
        return render(request, 'home/payment.html', {'place': place, 'total_price': total_price,'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY})

   
     


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
        
        if date:
            places = places.filter(date=date)
        
        if flight_class:
            places = places.filter(flight_class=flight_class)

        
        return render(request, 'shop.html', {'places': places})
    else:
        return render(request, 'home/index.html')
def success(request):
        return render(request,'home/success.html',{})




