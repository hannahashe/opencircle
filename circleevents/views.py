from django.shortcuts import render

from django.views.generic import ListView
from django.utils import timezone

from .models import Event

# Events List View below, using Django's generic ListView to
# display approved events only from ordered by published date.


class EventListView(ListView):
    """
    This view is responsible for displaying a list of events.
     It uses the Event model to retrieve the events from the database.
     The template used to render the list of events is "circleevents/event_list.html".
     The context variable that will be used in the template to access the list of events is "events".
    """
    model = Event
    template_name = "circleevents/event_list.html"
    context_object_name = "events"
    """
    Override the get_queryset method to filter events 
    based on their status and published date.
    Only events with a status of "approved" and 
    a published date that is less than or 
    equal to the current time will be included in the queryset.
    The events will be ordered by their published date in descending order.
    """
    def get_queryset(self):
        return Event.objects.filter(
            status="approved",
            published_at__lte=timezone.now()
        ).order_by("-published_at")
