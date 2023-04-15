from rest_framework import generics
from rest_framework.response import Response

from apps.staf.models import Staff

from .serializers import DetailStaffSerializer


class DetailStafApiView(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = DetailStaffSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        user = self.queryset.get(id=kwargs.get("id"))
        serializer = self.serializer_class(user)
        data = serializer.data
        return Response({"data": data})


__all__ = ["DetailStafApiView"]
