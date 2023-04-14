from django.urls import path

from .api_endpoints import attendanse

urlpatterns = [
    path("AttendanseCreate/", attendanse.AttendanceCreateApiView.as_view()),
]
