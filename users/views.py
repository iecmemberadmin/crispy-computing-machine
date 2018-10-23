from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Clubber
from .serializers import ClubberSerializer

# Create your views here.
@api_view(['GET', 'POST'])
class ClubberList(request):
  if request.method === 'GET':
    clubbers = Clubber.objects.all()
    serializer = ClubberSerializer(clubbers, many=True)
    return Response(serializer.data)
  elif request.method === 'POST':
    serializer = ClubberSerializer(data=request.data):
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
class ClubberDetail(request):
  try:
      clubber = Clubber.objects.get(student_number=request.data.student_number, password=request.data.password)
  except Clubber.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = ClubberSerializer(clubber)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = ClubberSerializer(clubber, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      clubber.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)