from rest_framework import serializers
from .models import Motor
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
        
class MotorSerializer(serializers.ModelSerializer):
    owner  = UserSerializer(read_only=True) 
    
    class Meta:
        model = Motor
        fields = ['id', 'owner', 'car_type', 'RegNo'] 
        read_only_fields = ['owner']
        
    def validate_RegNo(self, value):
        if len(value) < 6:
            
            serializers.ValidationError("Sorry The regNo should atleast 6 characters")      
        
        return value    