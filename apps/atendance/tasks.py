from datetime import datetime

from .models import Attendance
from apps.staf.models import Staff
from .api_endpoints.attendanse.AttendenseCreate import AttendanceSerializer

from celery import shared_task


@shared_task
def create_attendance(staff_id):
    staff = Staff.objects.get(id=staff_id)
    if staff not in Attendance.objects.filter(date=datetime.today()):
        status = Attendance.objects.create(staff=staff, status="kelmagan", date=datetime.today())
        return AttendanceSerializer(status).data










