from rest_framework import serializers
from .models import Position

class PositionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Position
    fields = ('id', 'committee', 'level', 'project', 'number_of_people', 'job_description', 'objectives', 'timeline', 'important_skills', 'challenges_faced', 'opportunities', 'role_history', 'document_resources', 'resources')