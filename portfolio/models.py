
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile


class Portfolio(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
  title = models.CharField(max_length=128)
  content = models.TextField(null=True, blank=True)

  date = models.DateField(blank=True, default=datetime.now)

  def __str__(self):
    return f'[{self.pk}]{self.title} by {self.user}'



class PostImage(models.Model):
  post = models.OneToOneField(Portfolio, on_delete=models.CASCADE, related_name='image', primary_key=True, unique=True)
  image = models.ImageField(upload_to='portfolio/img/', null=True, blank=True, default='')

  def __int__(self):
    return self.id
  def __str__(self):
    return f'img: {self.pk}) {self.post}'

class PostFile(models.Model):
  post = models.OneToOneField(Portfolio, on_delete=models.CASCADE, related_name='file', primary_key=True, unique=True)
  file = models.ImageField(upload_to='portfolio/file/', null=True, blank=True)

  def __int__(self):
    return self.id
  def __str__(self):
    return f'file: {self.pk}) {self.post}'

