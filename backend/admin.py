from django.contrib import admin
from .models import *


class CheckTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time', 'last_activity')


class CheckLocationAdmin(admin.ModelAdmin):
    list_display = ("name","longitude","width","width_window","country","city","region","timezone","create_at")


admin.site.register(CheckTime, CheckTimeAdmin)
admin.site.register(CheckLocation, CheckLocationAdmin)
# Register your models here.
