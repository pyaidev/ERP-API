from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.project.models import Project

from .serializers import ProjectDeleteSerializer


class DeleteProjectApiView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDeleteSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "slug"


__all__ = ["DeleteProjectApiView"]
