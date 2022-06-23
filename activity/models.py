from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Profile

class Field(models.Model):
  name=models.CharField(max_length=50, unique=True)
  slug=models.SlugField(max_length=200, unique=True, allow_unicode=True)

  def __str__(self):
    return self.name

class Tag(models.Model):
  name=models.CharField(max_length=50, unique=True)
  slug=models.SlugField(max_length=200, unique=True, allow_unicode=True)

  def __str__(self):
    return self.name

class Activity(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', default='1')
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, default='1')
  title = models.CharField(max_length=300, default='')
  tag = models.ManyToManyField(Tag, blank=True)
  company = models.CharField(max_length=100, default='')
  apply_period = models.DateField(null=True, blank=True)
  # field = models.CharField(max_length=300, blank=False, null=False, default='')
  field=models.ManyToManyField(Field, blank=True)
  actperiod = models.DateField(null=True, blank=True)
  personnel = models.IntegerField(default=0)
  detail = models.TextField(max_length=1000, blank=False, null=False, default='')
  apply_url = models.CharField(max_length=300, blank=True, null=True)
  img_url = models.CharField(max_length=300, blank=True, null=False)
  likes = models.ManyToManyField(User, blank=True)

    # 대외활동 이름 name
    # 관련태그 tag
    # 주최주관 company
    # 지원기간 applyperiod
    # 모집분야 field
    # 활동기간 actperiod
    # 모집인원 personnel
    # 상세설명 detail
    # 지원url apply-url
    # 이미지url img-url

  def __str__(self):
    return f'[{self.pk}]{self.title} by {self.author}'

