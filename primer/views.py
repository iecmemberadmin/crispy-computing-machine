from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Position, Application, Question
from .serializers import PositionSerializer, ApplicationSerializer, QuestionSerializer

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

@api_view(['GET', 'POST'])
def ApplicationList(request):
  if request.method == 'GET':
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ApplicationDetail(request):
  try:
      application = Application.objects.get(committee=request.GET['committee'], level=request.GET['level'], project=request.GET['project'], student_number=request.GET['student_number'])
  except Application.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = ApplicationSerializer(application)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = ApplicationSerializer(application, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      application.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def ApplicationUserDetail(request):
  try:
      applications = Application.objects.filter(student_number=request.GET['student_number'])
  except Application.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = ApplicationSerializer(applications, many=True)
      return Response(serializer.data)

@api_view(['GET', 'POST'])
def QuestionList(request):
  if request.method == 'GET':
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def QuestionDetail(request):
  try:
      question = Question.objects.get(question=request.GET['question'])
  except Question.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = QuestionSerializer(position)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = QuestionSerializer(position, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      question.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)