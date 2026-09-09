from rest_framework import serializers
from .models import PriceConfiguration, Booking
from motors.serializers import UserSerializer
from motors.serializers import MotorSerializer
from slots.serializers import SLotSerializer
from motors.models import Motor
from slots.models import Slot

class BookingSerializer(serializers.ModelSerializer):
    
    hourly_rate = serializers.ReadOnlyField()
    total_charges = serializers.ReadOnlyField()
    
    client = UserSerializer(read_only=True, source="user")
    
    motor = serializers.PrimaryKeyRelatedField(
    queryset=Motor.objects.all()
      )
    
    slot = serializers.PrimaryKeyRelatedField(
    queryset=Slot.objects.all()
      )
    
    class Meta:
        model = Booking
        fields = [
                  'id',
                  'client', 
                  'motor', 
                  'slot',
                  'start_time',
                  'end_time',
                  'hourly_rate',
                  'total_charges', 
                  'status'
                  ]
        
        read_only_fields = [
            'client',
            'hourly_rate',
            'total_charges',
            'status'
            ]
        

