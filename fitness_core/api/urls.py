from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.goals.goals import GoalsViewSet

router = DefaultRouter()
router.register(r'goals', GoalsViewSet, basename='goal')

urlpatterns = [
    path('', include(router.urls))
]