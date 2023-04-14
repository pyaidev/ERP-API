from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.project.models import Project

from .serializers import ProjectUpdateSerializer


class UpdateProjectApiView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "slug"
