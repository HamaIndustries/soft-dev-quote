from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
import uuid

# Create your models here.

class profileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField( max_length = 50, blank = False, null = False)
    address1 = models.CharField( max_length =100, blank = False, null = False)
    address2 = models.CharField( max_length =100, blank = True, null = False)
    state = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField( max_length = 100, blank = False, null = False)
    zipcode = models.IntegerField()

     