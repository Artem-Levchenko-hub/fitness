from rest_framework import serializers
from .base import UserBaseSerializer
from apps.accounts.models import Goals

class ProfileSerializer(UserBaseSerializer):
    goals = serializers.PrimaryKeyRelatedField(
        queryset=Goals.objects.all(),
        required=False,
        allow_null=True
    )
    goals_title = serializers.CharField(
        source='goals.title',
        read_only=True,
        allow_null = True,
        default = '')
    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + [
            'height',
            'weight_body',
            'fat_percent',
            'goals_title',
            'goals'
            ]


