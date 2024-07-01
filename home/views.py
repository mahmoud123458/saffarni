from django.shortcuts import render

from . models import Place,Continent, UserPayment
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from search.models import Hotel
from django.contrib.auth.models import User
from accounts.models import Profile
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe
import time

# Create your views here.
def home(request):
    continent = request.GET.get('continent')
    
    places = Place.objects.all()
    hotels = Hotel.objects.all()
    countries = Place.objects.values('country').distinct() 
    continents = Continent.objects.all()
    
    if continent:
        places = places.filter(continent=continent)
        return render(request, 'shop.html', {'places': places})
    else:
        return render(request, 'home/index.html', {'places': places, 'countries': countries, 'continents': continents,'hotels':hotels})



@login_required
def home_detail(request,slug):
   
    places_detail = Place.objects.get(slug=slug)
    
    return render(request,'home/detail.html',{'place':places_detail})




# from django.conf import settings
# from django.shortcuts import render
# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY






stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

@login_required(login_url='login')
def product_page(request):
    if request.method == 'POST':
        total_price = request.POST.get('total_price')
        
        if total_price is None:
            return render(request, 'home/product_page.html', {'error': 'Total price not provided'})
        
        try:
            total_price_int = int(total_price)
        except ValueError:
            return render(request, 'home/product_page.html', {'error': 'Invalid total price value'})

        try:
            price = stripe.Price.create(
                unit_amount=total_price_int,
                currency='usd',
                product_data={
                    'name': 'Trip Payment',
                },
            )
        except stripe.error.StripeError as e:
            return render(request, 'home/product_page.html', {'error': str(e)})

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_creation='always',
            success_url=settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
        return redirect(checkout_session.url, code=303)
    return render(request, 'home/product_page.html')

def payment_successful(request):
    checkout_session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    
    user_id = request.user.id
    user_payment = Profile.objects.get(user_id=user_id)
    user_payment.stripe_checkout_id = checkout_session_id
    user_payment.save()
    
    
    return render(request, 'home/payment_successful.html', {'customer': customer})

def payment_cancelled(request):
    return render(request, 'home/payment_cancelled.html')

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id')
        time.sleep(15)  # Introducing delay (if necessary)
        
        user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
        user_payment.payment_bool = True
        user_payment.save()

    return HttpResponse(status=200)





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
