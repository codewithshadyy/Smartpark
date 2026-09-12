from django.contrib import admin

from .models import PriceConfiguration, Booking


@admin.register(PriceConfiguration)

class PriceConfigurationAdmin(admin.ModelAdmin):
    list_display = ('motor_type', 'hourly_rate')
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'slot', 'motor', 'start_time', 'end_time', 'total_charges','status')    