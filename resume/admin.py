from django.contrib import admin

from .models import Resume, ResumeFile

admin.site.register(Resume)
admin.site.register(ResumeFile)