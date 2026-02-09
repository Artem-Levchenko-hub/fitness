from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
<<<<<<< HEAD
from api.serializers.goals.goals import GoalsSerializer
from apps.accounts.models import Goals


=======

from api.serializers.goals.goals import GoalsSerializer
from apps.accounts.models import Goals

>>>>>>> 2f362468418f10cbd60e4cf676e1518553849bad
class GoalsViewSet(viewsets.ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
    permission_classes = [IsAuthenticated]

<<<<<<< HEAD
    def perform_create(self, serializer):
=======
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    def perform_create(self, serializer):
        # Автоматически ставит request.user
>>>>>>> 2f362468418f10cbd60e4cf676e1518553849bad
        serializer.save(user=self.request.user)