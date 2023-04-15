from rest_framework import generics, permissions

from apps.staf.models import Staff

from .serializers import StaffSerializer


class StaffDeleteApiView(generics.DestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    lookup_field = "id"
    permission_classes = (permissions.IsAdminUser,)


__all__ = ["StaffDeleteApiView"]
