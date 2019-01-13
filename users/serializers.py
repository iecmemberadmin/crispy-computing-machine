from rest_framework import serializers
from .models import Clubber, Authentication, Announcement, ActiveProcess, ReaffedClubber

class ClubberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubber
        fields = ('student_number', 'first_name', 'middle_name', 'last_name', 'nick_name', 'committee', 'position', 'project', 'birthday', 'degree_program', 'mobile_number', 'email_address', 'permanent_address', 'present_address', 'emergency_name', 'emergency_relationship', 'emergency_contact')

class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication
        fields = ('clubber', 'password')

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id','title', 'body', 'date_posted')

class ActiveProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveProcess
        fields = ('name', 'active')

class ReaffedClubberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaffedClubber
        fields = ('clubber', 'last_name', 'updated_db', 'submitted_docs', 'paid_fee')