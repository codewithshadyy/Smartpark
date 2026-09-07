
from rest_framework import serializers
from .models import Slot

class SLotSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Slot
        fields = ['id', 'number', 'status']
        
   
        
         