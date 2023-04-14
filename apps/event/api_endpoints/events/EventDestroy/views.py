from rest_framework import generics
from .serializers import EventDeleteSerializer
from apps.event.models import Event


class EventApiDeleteView(generics.DestroyAPIView):
    serializer_class = EventDeleteSerializer
    queryset = Event.objects.all()

    lookup_field = "slug"



