from rest_framework import generics

from apps.event.models import Event

from .serializers import EventDeleteSerializer


class EventApiDeleteView(generics.DestroyAPIView):
    serializer_class = EventDeleteSerializer
    queryset = Event.objects.all()

    lookup_field = "slug"
