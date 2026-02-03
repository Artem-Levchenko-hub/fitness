from django.contrib import admin

from .models import MuscleGroup, Exercise, WorkoutTemplate, ExerciseTemplate, RealSession, Set

@admin.register(MuscleGroup)
class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = ('title',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_muscles', 'description')
    search_fields = ('title',)
    list_filter = ('muscles',)

    def get_muscles(self, obj):
        return ', '.join(m.title for m in obj.muscles.all())
    get_muscles.short_description = 'Мышечные группы'

@admin.register(WorkoutTemplate)
class WorkoutTemplateAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(ExerciseTemplate)
class ExerciseTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'exercise',
        'amount_sets',
        'reps',
        'workout_template')
    search_fields = ('exercise__title', 'workout_template__title', )
    list_filter = ('exercise', 'workout_template', )

@admin.register(RealSession)
class RealSessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'template_session_title', 'comment')
    search_fields = ('template_session__title', 'comment', )
    list_filter = ('date', )

    def template_session_title(self, obj):
        return obj.template_session.title
    
@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'real_reps', 'weight', 'session_set')
    search_fields = ('exercise__title', 'session_set',)
    search_fields = ('exercise__title', 'session_set',)