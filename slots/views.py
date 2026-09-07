from rest_framework import viewsets
from .models import Slot
from .serializers import SLotSerializer
from rest_framework.response import Response


class SlotViewSet(viewsets.ModelViewSet):
    
    viewsets = Slot.objects.all()
    serializer_class = SLotSerializer
