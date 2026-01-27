from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    height = models.IntegerField(verbose_name='Рост(см)')
    weight_body = models.DecimalField(decimal_places=1, verbose_name='Вес(кг)')
    fat_percent = models.DecimalField(decimal_places=1, verbose_name='Процент подкожного жира(%)')
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
class Goals(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='goals',
        verbose_name='Пользователь',
        )
    
    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.title