from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_organiser = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    profile_img = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Event(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    organiser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events"
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True, null=True)

    venue_name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)

    ticket_url = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)

    # Accessibility booleans
    step_free_access = models.BooleanField(default=False)
    accessible_toilet = models.BooleanField(default=False)
    seating_available = models.BooleanField(default=False)
    quiet_space = models.BooleanField(default=False)

    access_notes = models.TextField(blank=True)
    sensory_notes = models.TextField(blank=True)
    safespace_notes = models.TextField(blank=True)

    event_img = models.URLField(blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    TYPE_CHOICES = [
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]
    
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="notifications"
    )

    notification_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.notification_type} - {self.event.title}"
