from rest_framework import serializers
from django.contrib.auth.models import User
#from .models import login


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        #fields = '_ _all_ _'