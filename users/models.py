from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.

class Clubber(models.Model):
  COMMITTEES = [
    ('Executive', 'Executive'), 
    ('Academics', 'Academics'), 
    ('Externals', 'Externals'), 
    ('Extracurricular', 'Extracurricular'), 
    ('Finance', 'Finance'), 
    ('Internals', 'Internals'), 
    ('Membership', 'Membership'), 
    ('Publicity', 'Publicity'),
    ('TBA', 'TBA')
  ]
  POSITIONS = [
    ('President', 'President'),
    ('Vice President', 'Vice President'),
    ('Executive Secretary', 'Executive Secretary'),
    ('Associate Secretary', 'Associate Secretary'),
    ('Director', 'Director'),
    ('Project Manager', 'Project Manager'),
    ('Member', 'Member'),
    ('TBA', 'TBA')
  ]
  CANDIES = [
    ('Chocnut', 'Chocnut'),
    ('Choco Choco', 'Choco Choco'),
    ('Flat Tops', 'Flat Tops'),
    ('Potchi', 'Potchi')
  ]
  student_number = models.CharField(max_length=9, primary_key=True)
  first_name = models.CharField(max_length=100)
  middle_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  nick_name = models.CharField(max_length=100)
  committee = models.CharField(max_length=100, choices=COMMITTEES, default='')
  position = models.CharField(max_length=100, choices=POSITIONS, default='')
  project = models.CharField(max_length=100)
  birthday = models.DateField()
  degree_program = models.CharField(max_length=100)
  mobile_number = models.CharField(max_length=100)
  email_address = models.CharField(max_length=100)
  present_address = models.CharField(max_length=100)
  permanent_address = models.CharField(max_length=100)
  emergency_name = models.CharField(max_length=100)
  emergency_relationship = models.CharField(max_length=100)
  emergency_contact = models.CharField(max_length=100)
  carpool_capacity = models.IntegerField(default=0)
  av_equipment = models.CharField(max_length=100, default='')
  sports_equipment = models.CharField(max_length=100, default='')
  instruments = models.CharField(max_length=100, default='')
  current_subjects = models.CharField(max_length=255, default='')
  closest_friends = models.CharField(max_length=255, default='')
  ieaid_company = models.CharField(max_length=100, default='')
  ieaid_contactperson = models.CharField(max_length=100, default='')
  ieaid_contactdetails = models.CharField(max_length=100, default='')
  candy = models.CharField(max_length=100, choices=CANDIES, default='')

  def __str__(self):
    return "%s %s" % (self.student_number, self.last_name)

class Authentication(models.Model): 
  clubber = models.OneToOneField(Clubber, on_delete=models.CASCADE, primary_key=True)
  password = models.CharField(max_length=250)

  class Meta:
    ordering = ('clubber',)

  def __str__(self):
    return self.clubber.student_number

class Announcement(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  date_posted = models.DateTimeField(auto_now_add=True)
  tags = models.CharField(max_length=100)

  class Meta:
    ordering = ('date_posted',)

  def __str__(self):
    return self.title

class ActiveProcess(models.Model):
  name = models.CharField(max_length=100, primary_key=True)
  active = models.BooleanField()

  def __str__(self):
    return self.name

class ReaffedClubber(models.Model):
  clubber = models.OneToOneField(Clubber, on_delete=models.CASCADE, primary_key=True)
  last_name = models.CharField(max_length=100)
  nick_name = models.CharField(max_length=100, default='')
  updated_db = models.BooleanField()
  submitted_docs = models.BooleanField()
  paid_fee = models.BooleanField()
  read_contract = models.BooleanField(default=False)
  ew_participation = models.BooleanField(default=False)
  ew_jersey = models.BooleanField(default=False)

  def __str__(self):
    return '%s %s' % (self.clubber.student_number, self.last_name)

class Pending(models.Model):
  COMMITTEES = [
    ('Executive', 'Executive'), 
    ('Academics', 'Academics'), 
    ('Externals', 'Externals'), 
    ('Extracurricular', 'Extracurricular'), 
    ('Finance', 'Finance'), 
    ('Internals', 'Internals'), 
    ('Membership', 'Membership'), 
    ('Publicity', 'Publicity'),
    ('TBA', 'TBA')
  ]
  POSITIONS = [
    ('President', 'President'),
    ('Vice President', 'Vice President'),
    ('Executive Secretary', 'Executive Secretary'),
    ('Associate Secretary', 'Associate Secretary'),
    ('Director', 'Director'),
    ('Project Manager', 'Project Manager'),
    ('Member', 'Member'),
    ('TBA', 'TBA')
  ]
  CANDIES = [
    ('Chocnut', 'Chocnut'),
    ('Choco Choco', 'Choco Choco'),
    ('Flat Tops', 'Flat Tops'),
    ('Potchi', 'Potchi')
  ]
  student_number = models.CharField(max_length=9, primary_key=True)
  first_name = models.CharField(max_length=100)
  middle_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  nick_name = models.CharField(max_length=100)
  committee = models.CharField(max_length=100, choices=COMMITTEES, default='')
  position = models.CharField(max_length=100, choices=POSITIONS, default='')
  project = models.CharField(max_length=100)
  birthday = models.DateField()
  degree_program = models.CharField(max_length=100)
  mobile_number = models.CharField(max_length=100)
  email_address = models.CharField(max_length=100)
  present_address = models.CharField(max_length=100)
  permanent_address = models.CharField(max_length=100)
  emergency_name = models.CharField(max_length=100)
  emergency_relationship = models.CharField(max_length=100)
  emergency_contact = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  carpool_capacity = models.IntegerField(default=0)
  av_equipment = models.CharField(max_length=100, default='')
  sports_equipment = models.CharField(max_length=100, default='')
  instruments = models.CharField(max_length=100, default='')
  current_subjects = models.CharField(max_length=255, default='')
  closest_friends = models.CharField(max_length=255, default='')
  ieaid_company = models.CharField(max_length=100, default='')
  ieaid_contactperson = models.CharField(max_length=100, default='')
  ieaid_contactdetails = models.CharField(max_length=100, default='')
  candy = models.CharField(max_length=100, choices=CANDIES, default='')

  def __str__(self):
    return "%s %s" % (self.student_number, self.last_name)

class Event(models.Model):
  name = models.CharField(max_length=255, primary_key=True)
  date = models.DateTimeField()
  location = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class Attendance(models.Model):
  eventclubber = models.CharField(max_length=255, primary_key=True)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  clubber = models.ForeignKey(Clubber, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  
  class Meta: 
    unique_together = (('event', 'clubber'),)

  def __str__(self):
    return "%s: %s" % (self.event, self.clubber)

class Admin(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)

  def __str__(self):
    return self.username
    