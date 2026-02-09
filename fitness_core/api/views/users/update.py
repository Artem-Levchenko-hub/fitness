from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers.users.update import ProfileUpdatesSerializer
from apps.accounts.models import CustomUser

class ProfileUpdateViewSet(

):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileUpdatesSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
    
    def get_object(self):
        return self.request.user