from django.shortcuts import render
from rest_framework import generics
from .models import Clubber
from .serializers import ClubberSerializer

# Create your views here.
class ClubberList(generics.ListCreateAPIView):
  queryset = Clubber.objects.all()
  serializer_class = ClubberSerializer

class ClubberDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Clubber.objects.all()
  serializer_class = ClubberSerializer