from django.urls import path
from .views import EventListView, EventDetailView, profile_view, organiser_test_view


urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("profile/", profile_view, name="profile"),
    path("organiser-test/", organiser_test_view, name="organiser_test"),
    path("<slug:slug>/", EventDetailView.as_view(), name="event_detail"),
]
