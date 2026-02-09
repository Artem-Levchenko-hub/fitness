from rest_framework import serializers
from apps.accounts.models import Goals


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = [
            'id',
            'title',
        ]