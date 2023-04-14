from rest_framework import generics
from .serializers import EventDetailSerializer
from apps.event.models import Event


class EventApiDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    lookup_field = "slug"

