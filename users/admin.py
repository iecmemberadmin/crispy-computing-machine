from django.contrib import admin
from . models import Clubber, Authentication, Announcement

# Register your models here.
admin.site.register(Clubber)
admin.site.register(Authentication)
admin.site.register(Announcement)