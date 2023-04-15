from rest_framework import generics

from apps.event.models import Event

from .serializers import EventListSerializer


class EventListApiView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


__all__ = ["EventListApiView"]
