from rest_framework.serializers import ModelSerializer

from apps.event.models import Event


class EventDeleteSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ("slug",)
