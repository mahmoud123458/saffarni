import django_filters
from .models import Hotel

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'name': ['icontains'],
            'features1': ['exact'],
            'features2': ['exact'],
            'features3': ['exact'],
            'price': ['exact', 'lt', 'gt'],
        }
        order_by = ['name', 'features1', 'features2', 'features3', 'price']
