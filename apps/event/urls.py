from django.urls import path

from .api_endpoints import events

app_name = "event"

urlpatterns = [
    path("EventList/", events.EventListApiView.as_view(), name="event-list"),
    path("EventCreate/", events.EventApiCreate.as_view(), name = "event-create"),
    path("EventDelete/<slug:slug>/", events.EventApiDeleteView.as_view(), name = "event-delete"),
    path("EventDetail/<slug:slug>/", events.EventApiDetail.as_view(), name = "event-detail"),
    path("EventUpdate/<slug:slug>/", events.EventApiUpdate.as_view(), name = "event-update"),
]
