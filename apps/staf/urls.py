from django.urls import path

from .api_endpoints import staff

urlpatterns = [
    path("staff/<int:id>/", staff.DetailStafApiView.as_view()),
]
