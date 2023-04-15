from django.urls import path

from .api_endpoints import staff

urlpatterns = [
    path("Detail/<int:id>/", staff.DetailStafApiView.as_view()),
    path("List-Create/", staff.StaffCreateApiView.as_view()),
    path("<int:id>/attendance/", staff.StaffDeleteApiView.as_view()),
]
