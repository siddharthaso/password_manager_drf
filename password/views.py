from rest_framework import viewsets
from .serializers import PasswordSerializer
from .models import Passwords

class PasswordViewSet (viewsets.ModelViewSet):
    queryset = Passwords.objects.all()
    serializer_class = PasswordSerializer
