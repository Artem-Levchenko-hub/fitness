from django.db import models
from django.conf import settings

class MuscleGroup(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Мышечная группа'
        verbose_name_plural = 'Мышечные группы'

    def __str__(self):
        return self.title
class Exercise(models.Model):
    title = models.CharField(max_length=255)
    muscles = models.ManyToManyField(
        MuscleGroup,
        related_name='exersize',
        verbose_name = 'Мышечная группа')
    description = models.TextField(verbose_name='Описание техники')

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.title
    
class WorkoutTemplate(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название тренировочного плана')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='workout_templates',
        verbose_name='Создатель',
        on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Тренировочный шаблон'
        verbose_name_plural = 'Тренировочные шаблоны'
    def __str__(self):
        return self.title

class ExerciseTemplate(models.Model):
    