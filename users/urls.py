from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
  path('clubbers/', views.ClubberList),
  path('clubbers/<str:pk>/', views.ClubberDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)