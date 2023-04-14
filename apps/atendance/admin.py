from django.contrib import admin

from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["staf", "status"]
    list_display_links = ["staf", "status"]
    list_filter = ["staf", "status"]
    search_fields = ["staf", "status"]
    list_per_page = 10
