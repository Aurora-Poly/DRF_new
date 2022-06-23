from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class Resume(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)

  title = models.CharField(max_length=100) #제목
  file_upload = models.FileField(upload_to='resume/file/', blank=True) #파일
  date = models.DateField() #날짜
  comments = models.TextField() #코멘트