from django.views.generic import ListView, DetailView, TemplateView
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.utils.dateparse import parse_date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied

from .forms import EventForm, EditEventForm
from .decorators import organiser_required
from .models import Event


class HomeView(TemplateView):
    """
    This view is responsible for rendering the homepage of the application.
     It uses the TemplateView class from Django's generic views,
     which allows us to render a template without needing to define a model or
     queryset. The template used for the homepage is "circleevents/home.html".
     In the get_context_data method, we override the default context data to
     include a list of featured events. We filter the Event model to include
     only events with a status of "approved" and a startdate_time that is in
     the future, ordering them by their start datetime. We then slice the
     queryset to include only the first 3 events, which will be displayed as
     featured events on the homepage.
     """

    template_name = "circleevents/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_events"] = Event.objects.filter(
            status="approved"
        ).filter(start_datetime__gte=timezone.now()).order_by("start_datetime")[:3]
        return context


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
    paginate_by = 6
    """
    Override the get_queryset method to filter events
    based on their status and published date.
    Only events with a status of "approved" and
    a published date that is less than or
    equal to the current time will be included in the queryset.
    The events will be ordered by their start datetime in ascending order.
    """
    def get_queryset(self):
        queryset = Event.objects.filter(
            status="approved",
            published_at__lte=timezone.now()
        ).order_by("start_datetime")

        start_date = self.request.GET.get("start_date", "")
        end_date = self.request.GET.get("end_date", "")

        parsed_start_date = parse_date(start_date) if start_date else None
        parsed_end_date = parse_date(end_date) if end_date else None

        if parsed_start_date:
            queryset = queryset.filter(start_datetime__date__gte=parsed_start_date)

        if parsed_end_date:
            queryset = queryset.filter(start_datetime__date__lte=parsed_end_date)

        if self.request.GET.get("step_free_access") == "on":
            queryset = queryset.filter(step_free_access=True)

        if self.request.GET.get("accessible_toilet") == "on":
            queryset = queryset.filter(accessible_toilet=True)

        if self.request.GET.get("quiet_space") == "on":
            queryset = queryset.filter(quiet_space=True)

        if self.request.GET.get("seating_available") == "on":
            queryset = queryset.filter(seating_available=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["current_start_date"] = self.request.GET.get("start_date", "")
        context["current_end_date"] = self.request.GET.get("end_date", "")
        context["current_step_free_access"] = self.request.GET.get("step_free_access") == "on"
        context["current_accessible_toilet"] = self.request.GET.get("accessible_toilet") == "on"
        context["current_quiet_space"] = self.request.GET.get("quiet_space") == "on"
        context["current_seating_available"] = self.request.GET.get("seating_available") == "on"

        query_params = self.request.GET.copy()
        query_params.pop("page", None)
        encoded_query = query_params.urlencode()
        context["pagination_query"] = f"&{encoded_query}" if encoded_query else ""

        return context


class EventDetailView(DetailView):
    """
    This view is responsible for displaying the details of a single event.
    It uses the Event model to retrieve the event from the database.
    The template used to render the event details
    is "circleevents/event_detail.html".
    The context variable that will be used in
    the template to access the event is "event".
    """
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
    """
    This view is responsible for displaying the user's profile
    and allowing them to update their organiser status.
    It checks if the request method is POST, and if so,
    it updates the user's profile with the new organiser status
    and saves it to the database. If the request method is not POST,
    it simply renders the profile template with the user's profile information.
    This view also retrieves the events organised by the user
    and includes them in the context to be displayed on the profile page.
    This allows users to see and manage their events directly from their
    profile. Rejected events are shown with a link to edit them.
    In the edit event form, a message is shown to the user providing
    additional information about the reason for rejection and what
    they can do to get their event approved.
    """
    profile = request.user.profile

    if request.method == "POST":
        is_organiser = request.POST.get("is_organiser") == "on"
        profile.is_organiser = is_organiser
        profile.save()
        return redirect("profile")

    from .models import Event

    user_events = Event.objects.filter(organiser=request.user).order_by(
        "-created_at")

    # Find events that have been moderated but not yet notified
    # to the organiser and add notifications for them

    newly_moderated = Event.objects.filter(
        organiser=request.user,
        moderation_notified=False,
        status__in=["approved", "rejected"],
    )
    for event in newly_moderated:
        if event.status == "approved":
            messages.success(
                request,
                f"Event approved: \"{event.title}\" is now live.",
                )
        elif event.status == "rejected":
            messages.warning(
                request,
                f"Event not approved: \"{event.title}\" was rejected. Please review the moderator feedback below.",
                )
        event.moderation_notified = True
        event.save()

    context = {
        "profile": profile,
        "user_events": user_events,
    }
    return render(request, "circleevents/profile.html", context)


@organiser_required
def create_event(request):
    """
    This view is responsible for allowing organisers to create new events.
    It checks if the request method is POST, and if so, it processes the
    submitted form to create a new event. If the form is valid, it saves
    the event to the database with a status of "pending" and redirects
    the user to the event list page with a success message. If the request
    method is not POST, it simply renders the create event template with
    an empty form.
    """
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser = request.user
            event.status = "pending"
            event.save()

            messages.success(
                request,
                f"Event submitted: \"{event.title}\" is now pending moderator review."
            )
            return redirect("event_list")
    else:
        form = EventForm()

    return render(request, "circleevents/create_event.html", {"form": form})

@organiser_required
def edit_event(request, slug):
    """
    This view is responsible for allowing organisers to edit their
    existing events. It retrieves the event based on the provided slug and
    checks if the current user is the organiser of the event. If the user is
    not the organiser, it raises a PermissionDenied exception. If the request
    method is POST, it processes the submitted form to update the event. If the
    form is valid, it saves the updated event to the database with a status of
    "pending" and redirects the user to the event list page with an info
    message. If the request method is not POST, it simply renders the edit
    event template with the existing event information pre-filled in the form.
    """
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
            event.admin_comment = ""
            updated_event.save()

            messages.info(
                request,
                f"Event updated: \"{updated_event.title}\" has been resubmitted for moderator review.",
            )

            return redirect("event_list")
    else:
        form = EditEventForm(instance=event)

    return render(
        request,
        "circleevents/edit_event.html",
        {"form": form, "event": event},
    )


@organiser_required
@require_POST
def delete_event(request, slug):
    """
    This view is responsible for allowing organisers to delete
    their existing events. It retrieves the event based on the provided slug
    and checks if the current user is the organiser of the event.
    If the user is not the organiser, it raises a PermissionDenied exception.
    If the user is the organiser, it deletes the event from the database and
    redirects the user to the event list page with a success message.
    """
    event = get_object_or_404(Event, slug=slug)

    # Ownership check
    if event.organiser != request.user:
        raise PermissionDenied

    event.delete()

    messages.success(
        request,
        f"Event deleted: \"{event.title}\" has been removed."
    )
    return redirect("event_list")
