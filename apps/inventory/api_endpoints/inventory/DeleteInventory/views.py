from rest_framework import generics, permissions

from apps.inventory.models import Inventory

from ..CreateInventory.serializers import InventorySerializer


class InventoryDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    lookup_field = "id"


__all__ = ["InventoryDeleteApiView"]
