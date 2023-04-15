from django.contrib import admin

from .models import Internship


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "updated_at")
    list_filter = ("title", "slug", "created_at", "updated_at")
