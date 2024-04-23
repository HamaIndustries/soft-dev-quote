from django.db import models
from django.contrib.auth.models import User

class FuelQuote(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    gallons_requested = models.IntegerField()
    delivery_address = models.CharField(max_length=255)
    delivery_date = models.DateField()
    suggested_price_per_gallon = models.DecimalField(max_digits=6, decimal_places=2)
    total_amount_due = models.DecimalField(max_digits=10, decimal_places=2)