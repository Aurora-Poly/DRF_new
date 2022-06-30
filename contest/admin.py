from django.contrib import admin
from .models import Contest, Qualification, Award, Field

admin.site.register(Contest)


class QualificationAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class AwardAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}


class FieldAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(Qualification)
admin.site.register(Award)
admin.site.register(Field)
