from django.db import models

from apps.common.models import BaseModel


class Internship(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Internship"
        verbose_name_plural = "Internships"
        db_table = "internship"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
