from django.contrib import admin

from .models import Motor

@admin.register(Motor)


class MotorAdmin(admin.ModelAdmin):
    list_display = ['RegNo', 'owner', 'car_type']
    