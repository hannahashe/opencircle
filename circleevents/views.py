from django.views.generic import ListView, DetailView
from django.utils import timezone

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EventForm, EditEventForm
from .decorators import organiser_required
from .models import Event


class EventListView(ListView):
    """
    This view is responsible for displaying a list of events.
    It uses the Event model to retrieve the events from the database.
    The template used to render the list of events
    is "circleevents/event_list.html".
    The context variable that will be used in 
    the template to access the list of events is "events".
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


class EventDetailView(DetailView):
    model = Event
    template_name = "circleevents/event_detail.html"
    context_object_name = "event"

    def get_queryset(self):
        return Event.objects.filter(
            status="approved",
            published_at__lte=timezone.now()
        )


@login_required
def profile_view(request):
    profile = request.user.profile

    if request.method == "POST":
        is_organiser = request.POST.get("is_organiser") == "on"
        profile.is_organiser = is_organiser
        profile.save()
        return redirect("profile")

    context = {
        "profile": profile
    }
    return render(request, "circleevents/profile.html", context)


@organiser_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser = request.user
            event.status = "pending"
            event.save()

            messages.success(
                request,
                "Your event has been submitted and is awaiting approval."
            )
            return redirect("event_list")
    else:
        form = EventForm()

    return render(request, "circleevents/create_event.html", {"form": form})

@organiser_required
def edit_event(request, slug):
    event = get_object_or_404(Event, slug=slug)

    # Ownership check
    if event.organiser != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = EditEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            updated_event = form.save(commit=False)
            updated_event.status = "pending"
            updated_event.published_at = None
            updated_event.save()

            messages.success(
                request,
                "Your changes have been saved and the event has been resubmitted for approval."
            )
            return redirect("event_detail", slug=event.slug)
    else:
        form = EditEventForm(instance=event)

    return render(
        request,
        "circleevents/edit_event.html",
        {"form": form, "event": event},
    )
