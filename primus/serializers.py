# serializers.py
from rest_framework import serializers
from .models import UserPhoneNumber

class UserPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoneNumber
        fields = ['phone_number']
