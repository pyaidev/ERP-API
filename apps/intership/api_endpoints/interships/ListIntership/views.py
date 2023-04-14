from rest_framework import generics

from apps.intership.models import Internship

from .serializers import IntershipListSerializer


class IntershipListApiView(generics.ListAPIView):
    queryset = Internship.objects.all()
    serializer_class = IntershipListSerializer

    def get_queryset(self):
        return Internship.objects.filter(is_active=True)
