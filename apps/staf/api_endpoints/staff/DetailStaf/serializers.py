from rest_framework import serializers

from apps.atendance.api_endpoints.attendanse import AttendanceSerializer
from apps.atendance.models import Attendance
from apps.staf.models import Staff


class DetailStaffSerializer(serializers.Serializer):
    atendances = serializers.SerializerMethodField()

    def get_atendances(self, obj):
        attendances = Attendance.objects.filter(staff_id=obj.id)
        data = AttendanceSerializer(attendances, many=True).data
        for i in data:
            del i["staff"], i["created_at"], i["updated_at"], i["id"]

        return data

    class Meta:
        model = Staff

        fields = ("id", "staff__title", "email", "position", "atendances")
