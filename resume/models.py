from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from users.models import Profile
# Create your models here.
class Resume(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)

  title = models.CharField(max_length=100) #제목
  file_upload = models.FileField(upload_to='resume/file/', blank=True) #파일
  date = models.DateField(blank=True,  auto_now_add=True) #날짜
  comments = models.TextField() #코멘트

  def __str__(self):
    return f'[{self.pk}]{self.title} by {self.user}'


class ResumeFile(models.Model):
  post = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name='resume_file', primary_key=True, unique=True)
  file = models.ImageField(upload_to='resume/file/', null=True, blank=True)

  def __int__(self):
    return self.id
  def __str__(self):
    return f'file: {self.pk}) {self.post}'