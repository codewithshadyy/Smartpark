from rest_framework import serializers
from .models import PriceConfiguration, Booking
from motors.serializers import UserSerializer
from motors.serializers import MotorSerializer
from slots.serializers import SLotSerializer
from motors.models import Motor
from slots.models import Slot
from django.db import transaction

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
        
  
    @transaction.atomic
    
    def create(self, validated_data):
      
      slot = validated_data['slot']
      
      slot = Slot.objects.select_for_update().get(pk=slot.pk)
      
      if slot.status != Slot.SlotSatus.VACANT:
        raise serializers.ValidationError(
          {
             'slot': 'This parking slot is not available.'
          }
        )
      
      
      
      booking = Booking.objects.create(
        
        **validated_data
      )  
      
      slot.status = Slot.SlotSatus.BOOKED
      slot.save(update_fields=['status'])
      
      return booking
      
        
      
      
        

