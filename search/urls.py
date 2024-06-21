from django.urls import path
from . import views
urlpatterns = [
    path('',views.search,name='search'),
    path('payment_hotel/<str:slug>/', views.Payment_hotel, name='payment_hotel'),

]