from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Profile


class Portfolio(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
  title = models.CharField(max_length=128)
  category = models.CharField(max_length=128)
  content = models.TextField()

  date = models.DateField()
  head_img = models.ImageField(upload_to='portfolio/img/', blank=True)

  file_upload = models.FileField(upload_to='portfolio/file/', blank=True)



  def __str__(self):
    return f'[{self.pk}]{self.title}'