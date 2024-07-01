from django.urls import path
# from .views import CreateCheckoutSessionView, payment_success_view, payment_cancel_view
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<str:slug>',views.home_detail,name='detail'),

    path('search-flights/', views.search_flights, name='search_flights'),
    path('product_page', views.product_page, name='product_page'),
	path('payment_successful', views.payment_successful, name='payment_successful'),
	path('payment_cancelled', views.payment_cancelled, name='payment_cancelled'),
	path('stripe_webhook', views.stripe_webhook, name='stripe_webhook'),
    
]