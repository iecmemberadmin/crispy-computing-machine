from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.

class Clubber(models.Model):
  student_number = models.CharField(max_length=9, primary_key=True)
  password = models.CharField(max_length=250)

  class Meta:
    ordering = ('student_number',)

  def __str__(self):
    return self.student_number