from django.shortcuts import render

from django.views.generic import ListView
from django.utils import timezone

from .models import Event


class EventListView(ListView):
    model = Event
    template_name = "circleevents/event_list.html"
    context_object_name = "events"

    def get_queryset(self):
        return Event.objects.filter(
            status="approved",
            published_at__lte=timezone.now()
        ).order_by("-published_at")
