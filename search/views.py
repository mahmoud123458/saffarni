from django.shortcuts import render

from home.models import UserPayment
from .models import Hotel
from .filters import HotelFilter
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe
import time
from accounts.models import Profile  # Adjust the import path based on your actual Profile model location

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


stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

@login_required(login_url='login')
def product_page(request):
    if request.method == 'POST':
        total_price = request.POST.get('total_price')
        
        if total_price is None:
            return render(request, 'product_page_hotel.html', {'error': 'Total price not provided'})
        
        try:
            total_price_int = int(total_price)
        except ValueError:
            return render(request, 'product_page_hotel.html', {'error': 'Invalid total price value'})

        try:
            price = stripe.Price.create(
                unit_amount=total_price_int,
                currency='usd',
                product_data={
                    'name': 'Trip Payment',
                },
            )
        except stripe.error.StripeError as e:
            return render(request, 'product_page_hotel.html', {'error': str(e)})

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
    return render(request, 'product_page_hotel.html')

def payment_successful(request):
    checkout_session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    
    user_id = request.user.id
    user_payment = Profile.objects.get(user_id=user_id)
    user_payment.stripe_checkout_id = checkout_session_id
    user_payment.save()
    
    
    return render(request, 'payment_successful_hotel.html', {'customer': customer})

def payment_cancelled(request):
    return render(request, 'payment_cancelled_hotel.html')

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