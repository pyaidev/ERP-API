from django.contrib import admin

from .models import Category, Project


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "status", "created_at", "updated_at")
    list_display_links = (
        "title",
        "category",
    )
