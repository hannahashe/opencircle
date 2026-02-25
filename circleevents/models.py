from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

from cloudinary.models import CloudinaryField


# Custom user profile to extend the built-in User model,
# allowing for additional fields like is_organiser, bio, and profile_img.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_organiser = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    profile_img = CloudinaryField(
        "profile image",
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        Return the username of the associated User
        as the string representation of the Profile.
        """
        return self.user.username

# Custom Event model to store event details,
# including title, description, date/time, venue information,
# accessibility features, and status.
# The save method automatically generates
# a unique slug based on the event title and
# sets the published date when an event is approved.
# The model also includes fields for moderation status and admin comments,
# which are used to manage the event approval process.




class Event(models.Model):
    DEFAULT_REJECTION_COMMENT = (
        "Thanks for your submission. This event was not approved in its "
        "current form. Please review your event details carefully before resubmiting."
    )

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
    end_datetime = models.DateTimeField()

    venue_name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20, blank=True)

    ticket_url = models.URLField(blank=True)
    contact_email = models.EmailField()

    # Accessibility booleans
    step_free_access = models.BooleanField(default=False)
    accessible_toilet = models.BooleanField(default=False)
    seating_available = models.BooleanField(default=False)
    quiet_space = models.BooleanField(default=False)

    access_notes = models.TextField(blank=True)
    sensory_notes = models.TextField(blank=True)
    safespace_notes = models.TextField(blank=True)

    event_img = CloudinaryField(
        "event image",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending"
    )
    admin_comment = models.TextField(blank=True)
    moderation_notified = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """
        Return the title of the event as
        its string representation.
        """
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Event.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        if self.status == "approved" and self.published_at is None:
            self.published_at = timezone.now()

        if self.status == "rejected" and not self.admin_comment.strip():
            self.admin_comment = self.DEFAULT_REJECTION_COMMENT

        # Reset moderation notification if status changed
        if self.pk:
            previous = Event.objects.get(pk=self.pk)
            if previous.status != self.status:
                if self.status in ["approved", "rejected"]:
                    self.moderation_notified = False

        super(Event, self).save(*args, **kwargs)


# Notification model to store notifications for users,
# when their events are approved or rejected,
# and the message content of the notification.
# CURRENTLY NOT IN USE -
# PLANNED AS A FUTURE FEATURE FOR USER DASHBOARD NOTIFICATIONS.


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

    def save(self, *args, **kwargs):
        if self.notification_type == "approved":
            self.message = f"Your event '{self.event.title}' has been approved and is now live on Open Circle."
        elif self.notification_type == "rejected":
            self.message = f"Your event '{self.event.title}' has been rejected. Please see the message below for more details."
        super().save(*args, **kwargs)
