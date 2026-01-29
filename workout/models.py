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
        related_name='exercises',
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
    exercise = models.ForeignKey(
        Exercise, 
        on_delete=models.CASCADE,
        related_name='exercise_templates',
        verbose_name = 'Название упражнения'
    )
    amount_sets = models.IntegerField(verbose_name='Количество подходов')
    reps = models.IntegerField(verbose_name='Количество повторений')
    workout_template = models.ForeignKey(
        WorkoutTemplate,
        on_delete=models.CASCADE,
        related_name='exercise_templates',
        verbose_name='Тренировочный шаблон'
    )

    class Meta:
        verbose_name = 'Упражнение в тренировочном плане'
        verbose_name_plural = 'Упражнения в тренировочном плане'
    
    def __str__(self):
        return f'{self.exercise.title}: {self.amount_sets} x {self.reps}'
    
class RealSession(models.Model):
    date = models.DateTimeField(verbose_name='Дата и время тренировки')
    template_session = models.ForeignKey(
        WorkoutTemplate,
        on_delete=models.CASCADE,
        related_name='real_sessions',
        verbose_name='Шаблон тренировки'
    )
    comment = models.TextField(
        verbose_name='Комментарий по тренировке',
        blank=True)
    
    class Meta:
        verbose_name = 'Реальная сессия'
        verbose_name_plural = 'Реальные сессии'

class Set(models.Model):
    exercise = models.ForeignKey(
        Exercise, 
        on_delete=models.CASCADE,
        related_name='sets',
        verbose_name = 'Название упражнения'
    )
    real_reps = models.IntegerField(verbose_name='Повторения')
    weight = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        verbose_name='Вес снаряда(кг)'
        )
    session_set = models.ForeignKey(
            RealSession,
            on_delete=models.CASCADE,
            related_name='sets',
            verbose_name='Сессия'
    )
    def __str__(self):
        return f'{self.exercise.title}: {self.real_reps} x {self.weight} кг'