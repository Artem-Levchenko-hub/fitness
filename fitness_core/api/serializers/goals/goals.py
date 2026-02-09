from rest_framework import serializers
from apps.accounts.models import Goals


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = [
            'id',
<<<<<<< HEAD
            'title'
=======
            'title',
>>>>>>> 2f362468418f10cbd60e4cf676e1518553849bad
        ]