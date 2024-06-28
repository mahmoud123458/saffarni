from django.urls import path
from . import views
urlpatterns = [
    path('',views.search,name='search'),
    path('/book_hotel/<str:slug>',views.book_hotel,name='book_hotel'),
    path('/payment_hotel/<str:slug>/', views.Payment_hotel, name='payment_hotel'),

]