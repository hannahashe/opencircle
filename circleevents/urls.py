from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
]
