from rest_framework import serializers
from .models import Clubber

class ClubberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubber
        fields = ('student_number', 'password')