from datetime import datetime, time

from rest_framework import serializers

from apps.atendance.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("id", "staff", "delta_time", "created_at", "updated_at")

    def create(self, validated_data):
        delta = str(datetime.now() - datetime.combine(datetime.today(), time(11, 00)))
        validated_data["date"] = datetime.today()
        validated_data["time"] = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
        if "-" not in str(delta):
            hour, minutes = map(int, delta.split(":")[:2])

            if minutes > 0 or hour > 0:
                validated_data["status"] = "kechqoldi"
                validated_data["delta_time"] = f"{hour} soat {minutes} minut"
        else:
            validated_data["status"] = "vahtida_kelgan"

        return Attendance.objects.create(**validated_data)

    def validate(self, attrs):
        if Attendance.objects.filter(staff=attrs["staff"], date=datetime.today()).exists():
            raise serializers.ValidationError("Siz bugun yo'qlama qilindingiz")
        return attrs

