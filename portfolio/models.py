from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
from users.models import Profile


class Portfolio(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios')
  # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
  # title = models.CharField(max_length=128)
  # category = models.CharField(max_length=128)
  # content = models.TextField()

  # date = models.DateField()
  # head_img = models.ImageField(upload_to='portfolio/img/', blank=True)

  # file_upload = models.FileField(upload_to='portfolio/file/', blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
  title = models.CharField(max_length=128)
  category = models.CharField(max_length=128, blank=True)
  content = models.TextField(blank=True)

  date = models.DateField(blank=True, default=datetime.now)
  head_img = models.ImageField(upload_to='portfolio/img/', blank=True, null=True)

  file_upload = models.FileField(upload_to='portfolio/file/', blank=True, null=True)


  def __str__(self):
    return f'[{self.pk}]{self.title} by {self.user}'

def image_upload_path(instance, filename):
  return 'portfolio/file/'


class PostImage(models.Model):
  id = models.AutoField(primary_key=True)
  post = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='image')
  image = models.ImageField(upload_to='portfolio/img/')

  def __int__(self):
    return self.id
  def __str__(self):
    return f'img: {self.pk}) {self.post}'

  # class Meta:
  #   db_table = 'post_image'

class PostFile(models.Model):
  id = models.AutoField(primary_key=True)
  post = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='file')
  file = models.FileField(upload_to='portfolio/file/')

  def __int__(self):
    return self.id
  def __str__(self):
    return f'file: {self.pk}) {self.post}'

  # class Meta:
  #   db_table = 'post_image'