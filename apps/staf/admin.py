from django.contrib import admin

from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "position", "is_active"]
    list_filter = ["name", "email", "phone", "position", "is_active"]
    search_fields = ["name", "email", "phone", "position", "is_active"]
    list_per_page = 10
