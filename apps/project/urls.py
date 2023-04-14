from django.urls import path

from .api_endpoints import projects

urlpatterns = [
    path("ProjectList/", projects.ProjectListApiView.as_view()),
    path("ProjectCreate/", projects.CreateProjectApiView.as_view()),
    path("ProjectDetail/<slug:slug>/", projects.DeleteProjectApiView.as_view()),
    path("ProjectUpdate/<slug:slug>/", projects.UpdateProjectApiView.as_view()),
]
