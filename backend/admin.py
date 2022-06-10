from django.contrib import admin
from .models import *


class CheckTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time', 'last_activity')


admin.site.register(CheckTime, CheckTimeAdmin)
# Register your models here.
