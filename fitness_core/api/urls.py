from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.goals.goals import GoalsViewSet
from .views.users.registration import RegistrationViewSet
from .views.users.update import ProfileUpdateViewSet

router = DefaultRouter()
router.register(r'goals', GoalsViewSet, basename='goals')
router.register(r'registrations', RegistrationViewSet, basename='registrations')
router.register(r'updates', ProfileUpdateViewSet, basename='updates')
urlpatterns = [
    path('', include(router.urls)),
]
