from django.urls import path

from .api_endpoints import events

urlpatterns = [
    path("EventList/", events.EventListApiView.as_view()),
    path("EventCreate/", events.EventApiCreate.as_view()),
    path("EventDelete/<slug:slug>/", events.EventApiDeleteView.as_view()),
    path("EventDetail/<slug:slug>/", events.EventApiDetail.as_view()),
    path("EventUpdate/<slug:slug>/", events.EventApiUpdate.as_view()),
]
