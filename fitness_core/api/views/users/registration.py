from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.serializers.users.registration import RegistrationSerializer
from apps.accounts.models import CustomUser

class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]