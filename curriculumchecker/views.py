from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Curriculum, Course
from .serializers import CurriculumSerializer, CourseSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def CurriculumList(request):
  if request.method == 'GET':
    curriculums = Curriculum.objects.all()
    serializer = CurriculumSerializer(curriculums, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = CurriculumSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def CurriculumDetail(request):
  try:
      curriculum = Curriculum.objects.get(curriculum_name=request.GET['curriculum_name'])
  except Curriculum.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = CurriculumSerializer(curriculum)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = CurriculumSerializer(curriculum, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      curriculum.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def CourseList(request):
  if request.method == 'GET':
    courses = Course.objects.filter(curriculum=request.GET['curriculum'])
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def CourseDetail(request):
  try:
      course = Course.objects.get(curriculum=request.GET['curriculum'], course_title=request.GET['course_title'])
  except Course.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
      serializer = CourseSerializer(course)
      return Response(serializer.data)

  elif request.method == 'PUT':
      serializer = CourseSerializer(course, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
      course.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)