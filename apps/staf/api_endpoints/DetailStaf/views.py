from rest_framework import generics

from apps.atendance.api_endpoints.attendanse.AttendenseCreate.serializers import AttendanceSerializer
from apps.staf.models import Staf


class DetailStafApiView(generics.RetrieveAPIView):
    queryset = Staf.objects.all()
    serializer_class = AttendanceSerializer
    lookup_field = "id"

    def get_queryset(self):
        qs = self.queryset
        print(qs)
        return qs
