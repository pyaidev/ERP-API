from django.urls import path

from .api_endpoints import interships

urlpatterns = [
    path("IntershipList/", interships.IntershipListApiView.as_view()),
    path("IntershipCreate/", interships.CreateIntershipApiView.as_view()),
    path("IntershipDetail/<slug:slug>/", interships.DetailIntershipVIew.as_view()),
]
