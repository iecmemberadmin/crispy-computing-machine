from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.

class Position(models.Model):
  COMMITTEES = [
    ('Executive', 'Executive'), 
    ('Academics', 'Academics'), 
    ('Externals', 'Externals'), 
    ('Extracurricular', 'Extracurricular'), 
    ('Finance', 'Finance'), 
    ('Internals', 'Internals'), 
    ('Membership', 'Membership'), 
    ('Publicity', 'Publicity'),
    ('Matrix Project', 'Matrix Project')
  ]
  LEVELS = [
    ('Associate', 'Associate'),
    ('Director', 'Director'),
    ('Project Manager', 'Project Manager'),
    ('Project Head', 'Project Head'),
    ('Member', 'Member'),
  ]
  committee = models.CharField(max_length=100, choices=COMMITTEES, default='')
  level = models.CharField(max_length=100, choices=LEVELS, default='')
  project = models.CharField(max_length=100)
  number_of_people = models.IntegerField(default=1)
  job_description = ArrayField(models.TextField(blank=True))
  objectives = ArrayField(models.TextField(blank=True))
  timeline = ArrayField(models.TextField(blank=True))
  important_skills = ArrayField(models.TextField(blank=True))
  challenges_faced = ArrayField(models.TextField(blank=True))
  opportunities = ArrayField(models.TextField(blank=True))
  role_history = ArrayField(models.TextField(blank=True))
  document_resources = ArrayField(models.TextField(blank=True))
  resources = ArrayField(models.URLField(max_length=250))

  def __str__(self):
    return "(%s) %s - %s" % (self.committee, self.level, self.project)

class Application(models.Model):
  committee = models.CharField(max_length=100)
  level = models.CharField(max_length=100)
  project = models.CharField(max_length=100)
  name = models.CharField(max_length=250)
  student_number = models.CharField(max_length=250)
  answers = JSONField(blank=True, default=dict)

  def __str__(self):
    return "(%s) %s - %s: %s" % (self.committee, self.level, self.project, self.name)

class Question(models.Model):
  question = models.CharField(max_length=250)
  description = models.TextField(blank=True)

  def __str__(self):
    return self.question