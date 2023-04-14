from rest_framework.serializers import ModelSerializer

from apps.event.models import Event


class EventCreateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ("title", "description", "slug", "address", "start_date", "end_date", "is_active")
