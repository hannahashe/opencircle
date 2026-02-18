from django.urls import path
from .views import EventListView, EventDetailView, profile_view


urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("profile/", profile_view, name="profile"),
    path("<slug:slug>/", EventDetailView.as_view(), name="event_detail"),
]
