from django.db import models

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Profile
class Type(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, allow_unicode=True)
  def __str__(self):
    return f'[{self.pk}]{self.name}'

class Area(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, allow_unicode=True)
  def __str__(self):
    return f'[{self.pk}]{self.name}'

class Field(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, allow_unicode=True)
  def __str__(self):
    return f'[{self.pk}]{self.name}'

class Meet(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, allow_unicode=True)
  def __str__(self):
    return f'[{self.pk}]{self.name}'

class Volunteer(models.Model):
  title = models.CharField(max_length=100)
  act_period = models.CharField(max_length=200, blank=True)

  office =  models.CharField(max_length=100, blank=True)
  type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
  area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True)
  field = models.ForeignKey(Field, on_delete=models.CASCADE, blank=True, null=True)
  place = models.CharField(max_length=100, blank=True, null=True)
  meet = models.ForeignKey(Meet, on_delete=models.CASCADE, blank=True, null=True)
  apply_url= models.CharField(max_length=200, blank=True)


  def __str__(self):
    return f'[{self.pk}]{self.title}'