from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.event.models import Event

from .serializers import EventSerializerUpdate


class EventApiUpdate(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializerUpdate
    lookup_field = "slug"
    permission_classes = [IsAdminUser]
