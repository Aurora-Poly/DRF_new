from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Profile

class Club(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='club', default='1')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, default='1')
  title = models.CharField(max_length=100)
  personnel = models.IntegerField()
  content = models.TextField()
  date = models.DateField()
  contact = models.CharField(max_length=50, blank=True, null=True)
  apply_email = models.EmailField(blank=True, null=True)


  def __str__(self):
    return f'[{self.pk}]{self.title} by {self.author}'