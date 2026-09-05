from .serializers import Signup, PasswordResetRequestSerializer
from .models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt import token_blacklist
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Signup
    
class LogoutView(APIView):
    permission_classes = IsAuthenticated
    
    def post(self, request):
        
        try:
            refresh_token = request.data['refersh']
            token = RefreshToken(refresh_token)
            
            token.blacklist()
            
            return Response({
                "message": "Successfully logged out."
            }, status=status.HTTP_205_RESET_CONTENT)
            
        except Exception:
            return Response({
                "message":"Invalid request or token"
            }, status=status.HTTP_400_BAD_REQUEST)    
class PasswordResetView(generics.CreateAPIView):
    serializer_class = PasswordResetRequestSerializer
    
    def post(self, request):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"Message":"reset link sent to email"})
    
                
        


