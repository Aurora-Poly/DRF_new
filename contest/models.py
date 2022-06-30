from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Profile
class Qualification(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

  def __str__(self):
    return  f'[{self.pk}]qualifiaction: {self.name}'

class Award(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
  def __str__(self):
    return  f'[{self.pk}]Award: {self.name}'

class Field(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
  def __str__(self):
    return  f'[{self.pk}]Field: {self.name}'

class Contest(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contest', default='1')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, default='1')
  title = models.CharField(max_length=300,)
  tag = models.CharField(max_length=300)
  company = models.CharField(max_length=100)
  detail = models.TextField()
  # qualification = models.CharField(max_length=300)
  qualification = models.ManyToManyField(Qualification, blank=True) #자격요건
  award = models.ForeignKey(Award, null=True, on_delete=models.CASCADE, blank=True, default=None)
  field = models.ManyToManyField(Field, blank=True) #공모분야
  apply_url = models.CharField(max_length=300)
  img_url = models.CharField(max_length=300, blank=True, null=False)

  def __str__(self):
    return f'[{self.pk}]{self.title}'