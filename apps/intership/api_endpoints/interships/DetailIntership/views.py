from rest_framework import generics

from apps.intership.models import Internship

from .serializers import IntershipDetailSerializer


class DetailIntershipVIew(generics.RetrieveAPIView):
    queryset = Internship.objects.all()
    serializer_class = IntershipDetailSerializer
    lookup_field = "slug"
