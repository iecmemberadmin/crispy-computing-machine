from rest_framework import serializers
from .models import Clubber, Authentication

class ClubberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubber
        fields = ('student_number', 'first_name', 'middle_name', 'last_name', 'committee')

class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication
        fields = ('clubber', 'password')