from django.shortcuts import render
from home.models import Place
# Create your views here.

def shop(request):
    if request.method == 'POST':
        selected_country = request.POST.get('destination')
        if selected_country:
            places = Place.objects.filter(country=selected_country)
        else:
            places = Place.objects.all()
    else:
        places = Place.objects.all()

    context = {
        'places': places
    }
    return render(request, 'shop.html', context)