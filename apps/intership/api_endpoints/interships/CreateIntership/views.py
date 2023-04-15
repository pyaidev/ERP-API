from rest_framework import generics

from apps.intership.models import Internship

from .serializers import IntershipSerializer


class CreateIntershipApiView(generics.CreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = IntershipSerializer


__all__ = ["CreateIntershipApiView"]
