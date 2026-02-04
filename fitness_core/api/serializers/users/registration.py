from rest_framework import serializers
from .base import UserBaseSerializer

class RegistrationSerializer(UserBaseSerializer):
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type' 'password'}
        )
    class Meta:
        fields = UserBaseSerializer.Meta.fields + [
            'password',
            'password2'
        ]