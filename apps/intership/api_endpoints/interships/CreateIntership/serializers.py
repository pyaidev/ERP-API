from rest_framework import serializers

from apps.intership.models import Internship


class IntershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ("title", "description", "slug", "start_date", "end_date", "is_active")
