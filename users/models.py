from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
  name = models.CharField(unique = True, default='', max_length=100)
  univ = models.CharField(default='', max_length=100)
  dept = models.CharField(default='', max_length=100)
  age = models.IntegerField(default=0)

  def __str__(self):
    return f'[{self.pk}]{self.user}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

class ProfileImage(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_image', primary_key=True, unique=True)
  image = models.ImageField(upload_to='profile/img/', null=True, blank=True)

  def __int__(self):
    return self.id
  def __str__(self):
    return f'img: {self.pk}) {self.user}'