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
  path('auth/<str:pk>/', views.AuthDetail),
  path('reaff/', views.ReaffedClubbersList),
  path('reaff/<str:pk>/', views.ReaffedClubberDetail),
  path('pending/', views.PendingList), 
  path('pending/<str:pk>/', views.PendingDetail),
  path('events/', views.EventList),
  path('events/detail/', views.EventDetail),
  path('attendance/', views.AttendanceList),
  path('attendance/detail/', views.AttendanceDetail),
  path('auth/admin/', views.AdminList),
  path('auth/admin/<str:pk>/', views.ConfirmAdmin)
]

urlpatterns = format_suffix_patterns(urlpatterns)