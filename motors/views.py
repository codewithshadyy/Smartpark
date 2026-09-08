

from rest_framework.response import Response
from .serializers import MotorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Motor

class CreateMotorApiView()