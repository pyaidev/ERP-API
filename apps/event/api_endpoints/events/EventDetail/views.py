from rest_framework import generics

from apps.event.models import Event

from .serializers import EventDetailSerializer


class EventApiDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    lookup_field = "slug"


__all__ = ["EventApiDetail"]
