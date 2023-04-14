from rest_framework import serializers

from apps.project.models import Project


class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "slug", "dedline", "is_active")
