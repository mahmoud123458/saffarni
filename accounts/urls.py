from django.urls import path
from .import views
# from django.contrib.auth import views as auth_views

app_name ='accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),  
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.profile_edit,name='profile_edit'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
