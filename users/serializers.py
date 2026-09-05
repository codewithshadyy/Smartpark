
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.conf import settings

from django.core.mail  import send_mail

class Signup(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'role']
        
    def create(self, validated_data):
        
        username = validated_data['username']
        email= validated_data['email']
        password = validated_data['password']
        role =  validated_data.get('role')
        
        user = User.objects.create_user(**validated_data)
        
        return user
        
        
        
class PasswordResetRequestSerializer(serializers.Serializer):
    
    email = serializers.EmailField(unique=True)
    
    def validate(self, attrs):
        email = attrs["email"]
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator.make_token(user)
            reset_link = f"http://localhost:8000/auth/password-reset-confirm/{uidb64}/{token}/"
            
            
            send_mail(
                subject="Password reset Request",
                message=f"Reset your password: {reset_link}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )
            
        return attrs     
            
            
    
            
        
            