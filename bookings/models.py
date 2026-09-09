from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from motors.models import Motor
from slots.models import Slot
from django.utils import timezone
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError
from math import ceil
from decimal import Decimal




class PriceConfiguration(models.Model):
    
    motor_type = models.CharField(choices=Motor.CarType.choices, unique=True,
        help_text="The vehicle type this price applies to.")
    hourly_rate = models.DecimalField( max_digits=6, 
        decimal_places=2,
        help_text="Hourly rate charge for this vehicle type.")
    def __str__(self):
        return f"{self.get_motor_type.display()}: ${self.hourly_rate}/hr"
    
    
    
    
class Booking(models.Model):
    
    class BookingStatus(models.TextChoices):
        PAID = 'paid', 'Paid'
        RESERVED = 'reserved', 'Reserved'
        CANCELLED = 'Cancelled' , 'Cancelled'
      
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    motor =  models.ForeignKey(Motor, on_delete=models.PROTECT, related_name='bookings')
    slot = models.ForeignKey(Slot, on_delete=models.PROTECT, related_name="bookings")
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
    total_charges = models.DecimalField(max_digits=8, decimal_places=2, editable=False)
    status = models.CharField(max_length=20, choices=BookingStatus.choices, default=BookingStatus.RESERVED)
    
    
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")
    
    def calculate_duration_hours(self):
        if not self.start_time or not self.end_time:
            
            return 0
        
        duration = self.end_time - self.start_time
        hours = duration.total_seconds() / 3600
        return max(ceil(hours), 1)   
    
    def save(self, *args, **kwargs):
      try:
          price_config = PriceConfiguration.objects.get(motor_type = self.motor.car_type)
          self.hourly_rate = price_config.hourly_rate
          
      except PriceConfiguration.DoesNotExist:
          
          raise  ValidationError(
                 f"Pricing has not been configured for vehicle type: {self.motor.car_type}"
          )  
      hours_booked = self.calculate_duration_hours()
      self.total_charges = self.hourly_rate * Decimal(str(hours_booked))
        
      super().save(*args, **kwargs)    
 
        
        
    def __str__(self):
        return (
            f"Booking {self.id} - "
            f"{self.motor.RegNo} "
            f"(KSh {self.total_charges})"
        )
          
            
    
    
    
