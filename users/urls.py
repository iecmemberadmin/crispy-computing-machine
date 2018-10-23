from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
  path('clubbers/', views.ClubberList.as_view()),
  path('clubbers/<str:pk>/', views.ClubberDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)