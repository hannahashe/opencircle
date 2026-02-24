from django import forms
from .models import Event

# Form for organisers to create and edit events


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            widget = field.widget
            existing_classes = widget.attrs.get("class", "")

            if isinstance(widget, forms.CheckboxInput):
                widget.attrs["class"] = (
                    f"{existing_classes} form-check-input"
                ).strip()
            else:
                widget.attrs["class"] = (
                    f"{existing_classes} form-control event-form-control"
                ).strip()

            if isinstance(widget, forms.Textarea):
                widget.attrs.setdefault("rows", 4)

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


class EditEventForm(EventForm):
    class Meta(EventForm.Meta):
        exclude = ["title"]
