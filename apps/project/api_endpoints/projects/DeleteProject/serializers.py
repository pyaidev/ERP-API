from rest_framework import serializers

from apps.project.models import Project


class ProjectDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "dedline", "is_active")
