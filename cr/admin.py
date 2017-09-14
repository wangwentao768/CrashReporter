from django.contrib import admin

from .models import CrashLog, CrashLogAdmin

# Register your models here.
admin.site.register(CrashLog, CrashLogAdmin)