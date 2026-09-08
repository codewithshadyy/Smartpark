

from rest_framework.response import Response
from .serializers import MotorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Motor

class CreateMotorApiView(generics.CreateAPIView):
    
    serializer_class = MotorSerializer
    
    def post(self, request):
        
        serializer = MotorSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    
class GetMotorDetails(generics.ListAPIView):
    serializer_class = MotorSerializer
    queryset = Motor.objects.all()    
    