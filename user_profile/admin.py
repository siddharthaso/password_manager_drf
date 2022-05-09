from django.contrib import admin

from .models import Site,Tags,Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Site)