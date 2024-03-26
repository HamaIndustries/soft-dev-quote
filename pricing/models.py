from django.db import models
class FuelQuote(models.Model):
    gallons_requested = models.IntegerField()
    delivery_address = models.CharField(max_length=255)
    delivery_date = models.DateField()
    suggested_price_per_gallon = models.DecimalField(max_digits=6, decimal_places=2)
    total_amount_due = models.DecimalField(max_digits=10, decimal_places=2)