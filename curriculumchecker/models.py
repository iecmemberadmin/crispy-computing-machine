from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Curriculum(models.Model):
  curriculum_name = models.CharField(max_length=100, primary_key=True)
  
  def __str__(self):
    return self.curriculum_name
  
class Course(models.Model):
  curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
  course_title = models.CharField(max_length=100, primary_key=True)
  course_description = models.CharField(max_length=100)
  units = models.IntegerField(default=0)
  isJS = models.BooleanField()
  isSS = models.BooleanField()
  prerequisites = ArrayField(models.CharField(max_length=100), blank=True)
  corequisites = ArrayField(models.CharField(max_length=100), blank=True)

  def __str__(self):
    return "[%s] %s (%s)" % (self.curriculum, self.course_title, self.course_description)