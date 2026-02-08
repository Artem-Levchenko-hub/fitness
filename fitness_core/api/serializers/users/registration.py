from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _


from apps.accounts.models import CustomUser
from .base import UserBaseSerializer

class RegistrationSerializer(UserBaseSerializer):
    password = serializers.CharField(
        write_only = True,
        style={'input_type': 'password'},
        validators = [validate_password]
    )
    # password2 используется только для валидации, не входит в Meta.fields
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
        )
    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + [
            'password',
            'password2'
        ]
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': _('Пароли не совпадают')})
        if CustomUser.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'username': _('Это имя уже занято')})
        if CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': _('На эту почту уже зарегистрирован другой аккаунт')})
        
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2', None)
        
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

        

    
        