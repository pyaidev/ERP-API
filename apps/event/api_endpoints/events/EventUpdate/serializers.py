from rest_framework.serializers import ModelSerializer
from apps.event.models import Event


class EventSerializerUpdate(ModelSerializer):
    class Meta:
        model = Event
        fields = ("title", "description", "address", "start_date", "end_date", "is_active")
