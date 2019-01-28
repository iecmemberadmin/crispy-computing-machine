from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Clubber, Authentication, Announcement, ActiveProcess, ReaffedClubber, Pending, Event, Attendance
from .serializers import ClubberSerializer, AuthenticationSerializer, AnnouncementSerializer, ActiveProcessSerializer, ReaffedClubberSerializer, PendingSerializer, EventSerializer, AttendanceSerializer

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

@api_view(['GET', 'PUT', 'DELETE'])
def AuthDetail(request,pk):
  try:
      auth = Authentication.objects.get(clubber=pk)
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
def ActiveProcessList(request):
  if request.method == 'GET':
    process = ActiveProcess.objects.all()
    serializer = ActiveProcessSerializer(process, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ActiveProcessSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ActiveProcessDetail(request,pk):
  try:
      process = ActiveProcess.objects.get(name=pk)
  except ActiveProcess.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = ActiveProcessSerializer(process)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = ActiveProcessSerializer(process, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      process.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def ReaffedClubbersList(request):
  if request.method == 'GET':
    reaff = ReaffedClubber.objects.all()
    serializer = ReaffedClubberSerializer(reaff, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ReaffedClubberSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ReaffedClubberDetail(request,pk):
  try:
      reaff = ReaffedClubber.objects.get(clubber=pk)
  except ReaffedClubber.DoesNotExist:
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

@api_view(['GET', 'POST'])
def PendingList(request):
  if request.method == 'GET':
    pending = Pending.objects.all()
    serializer = PendingSerializer(pending, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = PendingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def PendingDetail(request,pk):
  try:
      pending = Pending.objects.get(student_number=pk)
  except Pending.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = PendingSerializer(pending)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = PendingSerializer(pending, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      pending.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def EventList(request):
  if request.method == 'GET':
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def EventDetail(request):
  try:
      event = Event.objects.get(name=request.GET['name'])
  except Event.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = EventSerializer(event)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = EventSerializer(event, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      event.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def AttendanceList(request):
  if request.method == 'GET':
    attendance = Attendance.objects.filter(event=request.GET['event'])
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = AttendanceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def AttendanceDetail(request):
  try:
      attendance = Attendance.objects.get(event=request.GET['event'], clubber=request.GET['clubber'])
  except Attendance.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = AttendanceSerializer(attendance)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = AttendanceSerializer(attendance, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      attendance.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)