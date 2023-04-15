from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.event.models import Event

from .serializers import EventCreateSerializer


class EventApiCreate(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [IsAdminUser]


__all__ = ["EventApiCreate"]
