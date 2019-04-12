from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Position
from .serializers import PositionSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def PositionList(request):
  if request.method == 'GET':
    positions = Position.objects.all()
    serializer = PositionSerializer(positions, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = PositionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def PositionDetail(request):
  try:
      position = Position.objects.get(committee=request.GET['committee'], level=request.GET['level'], project=request.GET['project'])
  except Position.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = PositionSerializer(position)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = PositionSerializer(position, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      position.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)