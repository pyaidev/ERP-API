from rest_framework import generics

from apps.project.models import Project

from .serializers import ProjectSerializer


class ProjectListApiView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


__all__ = ["ProjectListApiView"]
