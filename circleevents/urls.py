from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("<slug:slug>/", EventDetailView.as_view(), name="event_detail"),
]
