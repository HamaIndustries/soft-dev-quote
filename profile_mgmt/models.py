from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
import uuid

# Create your models here.

class User(models.Model):
    full_name = models.CharField( max_length = 50, blank = False, null = False)
    address1 = models.CharField( max_length =100, blank = False, null = False)
    address2 = models.CharField( max_length =100, blank = True, null = False)
    address1 = models.CharField( max_length =2, blank = False, null = False)
    city = models.CharField( max_length = 100, blank = False, null = False)
    zipcode = models.CharField(max_length=50, blank=False, null=False)


    zipcode_validator = [
        MinLengthValidator(limit_value=5, message="Zipcode must be at least 5 characters long"),
        MaxLengthValidator(limit_value=9, message="Zipcode must be at most 9 characters long")
    ]
     