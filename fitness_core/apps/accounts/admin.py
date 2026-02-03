from django.contrib import admin

from .models import CustomUser, Goals


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'height',
        'weight_body'
        )
    search_fields = ('username',)
    # Register your models here.
    list_filter = ('username',)

@admin.register(Goals)
class GoalsAdmin(admin.ModelAdmin):
    list_display = (
        'user__username',
        'title'
        )
    search_fields = ('user__username',)
    list_filter = ('user',)
