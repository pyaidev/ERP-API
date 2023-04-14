from rest_framework import generics
from .serializers import EventListSerializer
from apps.event.models import Event


class EventListApiView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


