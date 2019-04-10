from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from curriculumchecker import views

urlpatterns = [
  path('curriculums/list/', views.CurriculumList),
  path('curriculums/detail/', views.CurriculumDetail),
  path('courses/list/', views.CourseList),
  path('courses/detail/', views.CourseDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)