from django.urls import path
# from .views import CreateCheckoutSessionView, payment_success_view, payment_cancel_view
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<str:slug>',views.home_detail,name='detail'),
    path('payment/<str:slug>',views.Payment,name="payment"),
    path('search-flights/', views.search_flights, name='search_flights'),
    # path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('success/', views.success, name='success'),
    # path('cancel/', payment_cancel_view, name='cancel'),

   
]