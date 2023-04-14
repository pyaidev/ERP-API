from django.db import models

from apps.common.models import BaseModel


class Event(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    address = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        db_table = "event"

    def __str__(self):
        return self.title
