import time
from datetime import date, datetime, time, timedelta

from rest_framework import generics

from apps.atendance.models import Attendance

from .serializers import AttendanceSerializer


class AttendanceCreateApiView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    # def perform_create(self, serializer):
    #     data = self.request.data
    #     print(data.delta_time)

    #     # curr_time = time.strftime("%H:%M:%S", time.localtime())
    #     # a = curr_time-time(8,0)

    #     dt = datetime.now()-datetime.combine(date.today(), time(0, 5))
    #     print(str(dt))
    #     data["delta_time"]=dt
    #     # data.delta_time=dt
    #     # print("Current Time is :", curr_time)
    #     print(serializer)
    #     serializer.save()

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     ser
    #     print(*args)
    #     print(**kwargs)
    #     print(data.delta_time)
    #     print(data.get("staff"))
    #
    #     return super().post(request, *args, **kwargs)

    def get_queryset(self):
        qs = self.queryset
        print(qs)
        return qs
