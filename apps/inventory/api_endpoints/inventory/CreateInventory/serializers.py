from rest_framework import serializers

from apps.inventory.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("id", "name", "description", "quantity", "created_at", "updated_at")
