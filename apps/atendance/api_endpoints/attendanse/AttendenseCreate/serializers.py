from datetime import datetime, time

from rest_framework import serializers

from apps.atendance.models import Attendance
from apps.staf.models import Staff


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("id", "staff", "date", "time", "status", "delta_time", "created_at", "updated_at")

    def create(self, validated_data):
        print(validated_data)
        delta = str(datetime.now() - datetime.combine(datetime.today(), time(1, 20)))
        print(delta)
        # delta in minutes
        if "-" not in str(delta):
            hour, minutes = map(int, delta.split(":")[:2])

            if minutes > 0 or hour > 0:
                validated_data["status"] = "kechqoldi"
                validated_data["delta_time"] = f"{hour} soat {minutes} minut"
            else:
                validated_data["status"] = "vahtida kelgan"
        else:
            validated_data["status"] = "vahtida kelgan"

        # if delta.total_seconds()> 0:
        #     validated_data['status'] = "Late"
        return Attendance.objects.create(**validated_data)
