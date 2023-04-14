from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "address",
        "start_date",
        "end_date",
        "is_active",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "location", "description")
    list_filter = (
        "start_date",
        "end_date",
        "is_active",
    )
    list_per_page = 25
