from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    profile_view,
    create_event,
    edit_event
)


urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("profile/", profile_view, name="profile"),
    path("create/", create_event, name="create_event"),
    path("<slug:slug>/edit/", edit_event, name="edit_event"),
    path("<slug:slug>/", EventDetailView.as_view(), name="event_detail"),
]
