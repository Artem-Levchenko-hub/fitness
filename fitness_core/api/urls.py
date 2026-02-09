<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import include, path
>>>>>>> 2f362468418f10cbd60e4cf676e1518553849bad
from rest_framework.routers import DefaultRouter
from .views.goals.goals import GoalsViewSet

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'goals', GoalsViewSet, basename='goal')

urlpatterns = [
    path('', include(router.urls))
]
=======
router.register(r'goals', GoalsViewSet, basename='goals')

urlpatterns = [
    path('', include(router.urls)),
]
>>>>>>> 2f362468418f10cbd60e4cf676e1518553849bad
