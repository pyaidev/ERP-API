from django.db import models

from apps.common.models import BaseModel


class Staff(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
