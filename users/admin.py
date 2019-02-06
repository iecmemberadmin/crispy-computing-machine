from django.contrib import admin
from . models import Clubber, Authentication, Announcement, ActiveProcess, ReaffedClubber, Pending, Event, Admin, Attendance

# Register your models here.
admin.site.register(Clubber)
admin.site.register(Authentication)
admin.site.register(Announcement)
admin.site.register(ActiveProcess)
admin.site.register(ReaffedClubber)
admin.site.register(Pending)
admin.site.register(Event)
admin.site.register(Attendance)
admin.site.register(Admin)