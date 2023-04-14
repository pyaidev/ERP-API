from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import EventCreateSerializer
from apps.event.models import Event


class EventApiCreate(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [IsAdminUser]
