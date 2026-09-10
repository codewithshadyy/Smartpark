from django.shortcuts import render
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class BookingApiView(CreateAPIView):
    
    
    serializer_class = BookingSerializer
    
    def post(self, request):
        
        serializer = BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                'data':serializer.data
            })
        
        return Response({
            'errors':serializer.errors
        })
        
            
