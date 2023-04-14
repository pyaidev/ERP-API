from django.db import models

from apps.common.models import BaseModel

from .choosen import STATUS


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Project(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dedline = models.DateField()
    status = models.CharField(max_length=255, choices=STATUS, default="in_progress")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
