from datetime import datetime

from celery import shared_task

from apps.staf.models import Staff

from .api_endpoints.attendanse.AttendenseCreate import AttendanceSerializer
from .models import Attendance


@shared_task(name="create_attendance")
def create_attendance(staff_id):
    staff = Staff.objects.get(id=staff_id)
    if staff not in Attendance.objects.filter(date=datetime.today()):
        status = Attendance.objects.create(staff=staff, status="kelmagan", date=datetime.today())
        return AttendanceSerializer(status).data
