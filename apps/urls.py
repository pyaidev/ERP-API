from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.schema import swagger_urlpatterns

urlpatterns = [
    path("events/", include("apps.event.urls", namespace="event")),
    path("projects/", include("apps.project.urls")),
    path("interships/", include("apps.intership.urls")),
    path("attendanse/", include("apps.atendance.urls")),
    path("staff/", include("apps.staf.urls")),
    path("inventory/", include("apps.inventory.urls")),
]
