from django.urls import path

from .api_endpoints import staff

urlpatterns = [
    path("staff/<int:id>/", staff.DetailStafApiView.as_view()),
    path("staff/List-Create/", staff.StaffCreateApiView.as_view()),
    path("staff/<int:id>/attendance/", staff.StaffDeleteApiView.as_view()),
]
