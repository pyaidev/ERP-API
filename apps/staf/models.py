from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel


class Staff(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField(region="UZ")
    position = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staffs"
        db_table = "staff"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
