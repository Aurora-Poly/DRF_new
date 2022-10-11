from django.contrib import admin
from activity.models import Activity, Field, Target, Office, Prize

admin.site.register(Activity)

class FieldAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class TargetAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class OfficeAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

class PrizeAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(Field)
admin.site.register(Target)
admin.site.register(Office)
admin.site.register(Prize)
