from django.contrib import admin

from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "created_at", "updated_at")
    list_filter = ("name", "quantity", "created_at", "updated_at")
    search_fields = ("name", "quantity", "created_at", "updated_at")
    list_per_page = 20
