from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from primer import views

urlpatterns = [
  path('positions/all/', views.PositionList),
  path('positions/detail/', views.PositionDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)