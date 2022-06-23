from django.contrib import admin
from activity.models import Activity, Field, Tag

admin.site.register(Activity)

class FieldAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
admin.site.register(Field)
admin.site.register(Tag)