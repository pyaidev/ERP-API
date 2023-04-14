from rest_framework import serializers

from apps.staf.models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("id", "name", "surname", "position", "created_at", "updated_at")
