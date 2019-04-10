from rest_framework import serializers
from . models import Curriculum, Course

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('curriculum', 'course_title', 'course_description', 'units', 'isJS', 'isSS', 'prerequisites', 'corequisites')

