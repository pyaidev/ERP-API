from rest_framework import serializers

from apps.intership.models import Internship


class IntershipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ("title", "description", "start_date", "end_date", "is_active")
