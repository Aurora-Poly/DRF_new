from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Profile

class Contest(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contest', default='1')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, default='1')
  title = models.CharField(max_length=300,)
  tag = models.CharField(max_length=300)
  company = models.CharField(max_length=100)
  detail = models.TextField()
  qualification = models.CharField(max_length=300)
  award = models.CharField(max_length=100)
  field = models.CharField(max_length=300)
  apply_url = models.CharField(max_length=300)
  img_url = models.CharField(max_length=300, blank=True, null=False)

  def __str__(self):
    return f'[{self.pk}]{self.title}'