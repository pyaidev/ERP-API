from rest_framework import generics

from apps.atendance.models import Attendance

from .serializers import AttendanceSerializer


class AttendanceCreateApiView(generics.CreateAPIView):
    """Status va delta_time ni avtomatik hisoblaydi"""

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        qs = self.queryset
        return qs
