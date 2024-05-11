from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<str:slug>',views.home_detail,name='detail'),
    path('payment/<str:slug>',views.Payment,name="payment"),
   
]