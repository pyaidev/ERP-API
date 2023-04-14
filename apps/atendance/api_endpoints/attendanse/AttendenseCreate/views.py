from rest_framework import generics

from apps.atendance.models import Attendance

from .serializers import AttendanceSerializer


class AttendanceCreateApiView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        qs = self.queryset
        print(qs)
        return qs
