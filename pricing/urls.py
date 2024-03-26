from django.urls import path
from .views import create_fuel_quote

from . import views

app_name = "pricing"
urlpatterns = [
    path('fuelquote/', create_fuel_quote, name='create_fuel_quote'),
]