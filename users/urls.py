from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
  path('login/<str:pk>/', views.ConfirmAuthentication),
  path('login/', views.AuthenticationList),
  path('clubbers/', views.ClubberList),
  path('clubbers/<str:pk>/', views.ClubberDetail),
  path('announcements/', views.AnnouncementList),
  path('reaff/', views.ReaffList),
  path('reaff/<str:pk>/', views.ReaffDetail),
  path('reaffed/', views.ReaffedClubberList),
  path('reaffed/<str:pk>/', views.ReaffedClubberSemDetail),
  path('reaffed/<str:sem>/<str:sn>/', views.ReaffedClubberDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)