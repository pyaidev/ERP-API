from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.project.models import Project

from .serializers import ProjectCreateSerializer


class CreateProjectApiView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAdminUser]
