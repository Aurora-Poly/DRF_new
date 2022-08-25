from django.contrib import admin

from portfolio.models import Portfolio, PostImage, PostFile

admin.site.register(Portfolio)
admin.site.register(PostImage)
admin.site.register(PostFile)