from django.shortcuts import render
from home.models import Place
# Create your views here.
def shop(request):
    places = Place.objects.all()
    return render(request,'shop.html',{'places':places})