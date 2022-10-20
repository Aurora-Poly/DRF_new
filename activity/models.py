from django.db import models
from rest_framework.authtoken.admin import User
from users.models import Profile

#분야
class Field(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, allow_unicode=True)

  def __str__(self):
    return f'[{self.pk}]{self.name}'

#참가대상
class Target(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, allow_unicode=True)

  def __str__(self):
    return f'[{self.pk}]{self.name}'

#주최기관
class Office(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, allow_unicode=True)

  def __str__(self):
    return f'[{self.pk}]{self.name}'

#상금
class Prize(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, allow_unicode=True)

  def __str__(self):
    return f'[{self.pk}]{self.name}'

#대외활동
class Activity(models.Model):
  title = models.CharField(max_length=300)
  views = models.IntegerField(blank=True)
  prize = models.ForeignKey(Prize, on_delete=models.CASCADE, blank=True)
  office = models.ForeignKey(Office, on_delete=models.CASCADE, blank=True)
  juchae = models.CharField(max_length=100, blank=True)
  jukwan = models.CharField(max_length=100, blank=True)
  field = models.ManyToManyField(Field, blank=True)
  target = models. ManyToManyField(Target, blank=True)
  apply_period = models.CharField(max_length=200, blank=True)
  prize_1st = models.CharField(max_length=200, blank=True)
  apply_url = models.CharField(max_length=200, blank=True)
  image_url = models.CharField(max_length=200, blank=True)

  #좋아요
  likes = models.ManyToManyField(User, blank=True, related_name='like_posts')
  def like_count(self):
        return self.likes.count()

  def __str__(self):
    return f'[{self.pk}]{self.title}'

