from rest_framework import serializers
from .models import Clubber, Authentication

class ClubberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubber
        fields = ('student_number', 'first_name', 'middle_name', 'last_name', 'nick_name', 'committee', 'position', 'project', 'birthday', 'degree_program', 'mobile_number', 'email_address', 'permanent_address', 'present_address', 'emergency_name', 'emergency_relationship', 'emergency_contact')

class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication
        fields = ('clubber', 'password')