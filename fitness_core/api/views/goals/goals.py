from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers.goals.goals import GoalsSerializer
from apps.accounts.models import Goals

class GoalsViewSet(viewsets.ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    def perform_create(self, serializer):
        # Автоматически ставит request.user
        serializer.save(user=self.request.user)