from django.contrib import admin

from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["staff", "status"]
    list_display_links = ["staff", "status"]
    list_filter = ["staff", "status"]
    search_fields = ["staff", "status"]
    list_per_page = 10
