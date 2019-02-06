from rest_framework import serializers
from .models import Clubber, Authentication, Announcement, ActiveProcess, ReaffedClubber, Pending, Event, AttendanceNew, Admin

class ClubberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubber
        fields = ('student_number', 'first_name', 'middle_name', 'last_name', 'nick_name', 'committee', 'position', 'project', 'birthday', 'degree_program', 'mobile_number', 'email_address', 'permanent_address', 'present_address', 'emergency_name', 'emergency_relationship', 'emergency_contact', 'carpool_capacity', 'av_equipment', 'sports_equipment', 'instruments', 'current_subjects', 'closest_friends', 'ieaid_company', 'ieaid_contactperson', 'ieaid_contactdetails', 'candy')

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
        fields = ('clubber', 'last_name', 'nick_name', 'updated_db', 'submitted_docs', 'paid_fee', 'read_contract', 'ew_participation', 'ew_jersey')

class PendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = ('student_number', 'first_name', 'middle_name', 'last_name', 'nick_name', 'committee', 'position', 'project', 'birthday', 'degree_program', 'mobile_number', 'email_address', 'permanent_address', 'present_address', 'emergency_name', 'emergency_relationship', 'emergency_contact', 'carpool_capacity', 'av_equipment', 'sports_equipment', 'instruments','password', 'current_subjects', 'closest_friends', 'ieaid_company', 'ieaid_contactperson', 'ieaid_contactdetails', 'candy')

class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Event
        fields = ('name', 'date', 'location')

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceNew
        fields = ('event', 'clubber', 'name',)

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')