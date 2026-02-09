from rest_framework import serializers
from .base import UserBaseSerializer

class ProfileUpdatesSerializer(UserBaseSerializer):
    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + [
            'fat_percent',
            'weight_body',
            'height'
        ]
        read_only_fields = ['id']
        