from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
  path('login/<str:pk>/', views.ConfirmAuthentication),
  path('login/', views.AuthenticationList),
  path('clubbers/', views.ClubberList),
  path('clubbers/<str:pk>/', views.ClubberDetail),
  path('announcements/', views.AnnouncementList),
  path('proc/', views.ActiveProcessList),
  path('proc/<str:pk>/', views.ActiveProcessDetail),
  path('auth/', views.AuthenticationList),
  path('reaff/', views.ReaffedClubbersList),
  path('reaff/<str:pk>/', views.ReaffedClubberDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)