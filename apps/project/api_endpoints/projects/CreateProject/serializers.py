from rest_framework import serializers

from apps.project.models import Project


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title", "description", "dedline", "is_active")
