from rest_framework import serializers
from .base import UserBaseSerializer

class ProfileSerializer(UserBaseSerializer):
    fields = UserBaseSerializer.Meta.fields + ['height', 'weight_body', 'fat_percent']
    goals = serializers.S
