from rest_framework import serializers
from apps.accounts.models import CustomUser, Goals

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id']

