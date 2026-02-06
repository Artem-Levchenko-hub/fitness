from rest_framework import serializers
from apps.accounts.models import CustomUser, Goals

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',
                  'email',
                  'username',
                  'first_name',
                  'last_name'
                  ]
        read_only_fields = ['id']



