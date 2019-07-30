from django.contrib import admin
from core.models import Device
# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('url', 'access_token', 'user')
