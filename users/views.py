from .serializers import Signup
from .models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Signup


