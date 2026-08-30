from .serializers import Signup
from .models import User
from rest_framework.viewsets import ModelViewSet

class SignUpView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Signup


