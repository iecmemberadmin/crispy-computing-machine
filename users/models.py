from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.

class Clubber(models.Model):
  COMMITTEES = [
    ('execomm', 'Executive'), 
    ('acadcomm', 'Academics'), 
    ('externals', 'External Affairs'), 
    ('extracomm', 'Extracurricular Affairs'), 
    ('fincomm', 'Finance'), 
    ('Internal Affairs', 'Internal Affairs'), 
    ('memcomm', 'Membership'), 
    ('pubcomm', 'Publicity')
  ]
  student_number = models.CharField(max_length=9, primary_key=True)
  first_name = models.CharField(max_length=100)
  middle_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  committee = models.CharField(max_length=100, choices=COMMITTEES, default='')

  def __str__(self):
    return "%s %s" % (self.student_number, self.last_name)

class Authentication(models.Model): 
  clubber = models.OneToOneField(Clubber, on_delete=models.CASCADE, primary_key=True)
  password = models.CharField(max_length=250)

  class Meta:
    ordering = ('clubber',)

  def __str__(self):
    return self.clubber.student_number


