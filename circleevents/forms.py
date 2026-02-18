from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "start_datetime",
            "end_datetime",
            "venue_name",
            "address",
            "city",
            "postcode",
            "contact_email",
            "ticket_url",
            "step_free_access",
            "accessible_toilet",
            "seating_available",
            "quiet_space",
            "access_notes",
            "sensory_notes",
            "safespace_notes",
            "event_img",
        ]

        widgets = {
            "start_datetime": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
                ),
            "end_datetime": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
                ),
        }
