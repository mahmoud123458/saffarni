from django.urls import path
from .import views
urlpatterns = [
    path('/',views.blog,name='blog'), 
    path('read_more1',views.readMore1,name='read_more1'), 
    path('read_more2',views.readMore2,name='read_more2'),
    path('read_more3',views.readMore3,name='read_more3'),
    path('read_more4',views.readMore4,name='read_more4'),

]
