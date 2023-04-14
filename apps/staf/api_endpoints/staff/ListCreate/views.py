from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.staf.models import Staff

from .serializers import StaffSerializer


class StaffCreateApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
