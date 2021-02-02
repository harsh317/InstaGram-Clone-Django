from .views import registerInsta,profile
from django.urls import path

urlpatterns = [
    path('register/',registerInsta,name='register'),
    path('profile/',profile,name='profile'),
]