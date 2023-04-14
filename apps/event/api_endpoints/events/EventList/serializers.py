from rest_framework.serializers import ModelSerializer

from apps.event.models import Event


class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ("title", "address", "start_date", "end_date", "is_active")
