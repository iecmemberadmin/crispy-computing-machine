from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Clubber, Authentication, Announcement, Reaff, ReaffedClubber
from .serializers import ClubberSerializer, AuthenticationSerializer, AnnouncementSerializer, ReaffSerializer, ReaffedClubberSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def ClubberList(request):
  if request.method == 'GET':
    clubbers = Clubber.objects.all()
    serializer = ClubberSerializer(clubbers, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ClubberSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ClubberDetail(request,pk):
  try:
      clubber = Clubber.objects.get(student_number=pk)
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

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ConfirmAuthentication(request,pk):
  try:
      auth = Authentication.objects.get(clubber=pk, password=request.GET['password'])
  except Authentication.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = AuthenticationSerializer(auth)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = AuthenticationSerializer(auth, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      auth.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def AuthenticationList(request): 
  if request.method == 'GET':
    authentications = Authentication.objects.all()
    serializer = AuthenticationSerializer(authentications, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = AuthenticationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def AnnouncementList(request):
  if request.method == 'GET':
    announcements = Announcement.objects.all()
    serializer = AnnouncementSerializer(announcements, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = AnnouncementSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def ReaffList(request):
  if request.method == 'GET':
    reaffs = Reaff.objects.all()
    serializer = ReaffSerializer(reaffs, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ReaffSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ReaffDetail(request,pk):
  try:
      reaff = Reaff.objects.get(sem=pk)
  except Reaff.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = ReaffSerializer(reaff)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = ReaffSerializer(reaff, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      reaff.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def ReaffedClubberList(request):
  if request.method == 'GET':
    reaffs = ReaffedClubber.objects.all()
    serializer = ReaffedClubberSerializer(reaffs, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ReaffedClubberSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ReaffedClubberSemDetail(request,pk):
  try:
      reaff = ReaffedClubber.objects.filter(reaff=pk)
  except Reaff.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = ReaffedClubberSerializer(reaff, many=True)
      return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def ReaffedClubberDetail(request,sem,sn):
  try:
      reaff = ReaffedClubber.objects.get(reaff=sem, clubber=sn)
  except Reaff.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = ReaffedClubberSerializer(reaff)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = ReaffedClubberSerializer(reaff, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      reaff.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)