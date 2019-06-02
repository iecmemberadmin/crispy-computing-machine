from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from primer import views

urlpatterns = [
  path('positions/all/', views.PositionList),
  path('positions/detail/', views.PositionDetail),
  path('applications/all/', views.ApplicationList),
  path('applications/detail/', views.ApplicationDetail),
  path('applications/user/', views.ApplicationUserDetail),
  path('questions/all/', views.QuestionList),
  path('questions/detail/', views.QuestionDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)