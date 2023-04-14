from django.db import models

from apps.common.models import BaseModel


class Inventory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    total_price = models.FloatField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
