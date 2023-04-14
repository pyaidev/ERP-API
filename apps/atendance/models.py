from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.common.models import BaseModel
from apps.staf.models import Staff

from .choises import STATUS


class Attendance(BaseModel):
    staf = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default="kelmadi")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
        db_table = "attendance"
        ordering = ["-created_at"]

    def __str__(self):
        return self.staf.name
