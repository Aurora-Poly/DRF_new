from django.contrib import admin

from volunteer.models import Volunteer, Type, Field, Meet, Area

admin.site.register(Volunteer)

class TypeAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class AreaAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class FieldAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class MeetAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(Type)
admin.site.register(Field)
admin.site.register(Meet)
admin.site.register(Area)