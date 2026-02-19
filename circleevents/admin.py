from django.contrib import admin
from .models import Event, Profile, Notification


admin.site.register(Profile)
admin.site.register(Notification)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "organiser",
        "start_datetime",
        "published_at",
    )

    list_filter = (
        "status",
        "start_datetime",
    )

    search_fields = (
        "title",
        "organiser__username",
        "city",
        "postcode",
    )

    ordering = ("-created_at",)
