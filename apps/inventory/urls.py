from django.urls import path

from .api_endpoints import inventory

urlpatterns = [
    path("Retrive_Update_Destroy/<int:id>/", inventory.InventoryDeleteApiView.as_view()),
    path("inventory/List-Create/", inventory.InventoryCreateApiView.as_view()),
]
