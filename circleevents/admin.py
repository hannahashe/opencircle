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

    actions = ["approve_events"]

    def approve_events(self, request, queryset):
        updated = 0
        for event in queryset:
            if event.status != "approved":
                event.status = "approved"
                event.save()
                updated += 1
        self.message_user(
            request,
            f"{updated} event(s) have been successfully approved."
        )

    approve_events.short_description = "Approve selected events."