from django.contrib import admin

from .models import PriceConfiguration

@admin.register(PriceConfiguration)

class PriceConfigurationAdmin(admin.ModelAdmin):
    list_display = ('car_type', 'hourly_rate')
