from django.urls import path
from . import views
urlpatterns = [
    path('',views.search,name='search'),
    path('book_hotel/<str:slug>',views.book_hotel,name='book_hotel'),
    path('payment_successful_hotel/', views.payment_successful, name='payment_successful_hotel'),
    path('product_page_hotel',views.product_page,name='product_page_hotel'),
    path('payment_cancelled_hotel',views.payment_cancelled,name='payment_cancelled_hotel'),
    path('stripe_webhook_hotel',views.stripe_webhook,name='stripe_webhook_hotel'),
    
]