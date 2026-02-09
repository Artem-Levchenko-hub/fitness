from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers.goals.goals import GoalsSerializer
from apps.accounts.models import Goals


class GoalsViewSet(viewsets.ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)