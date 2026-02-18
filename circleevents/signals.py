from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    This signal receiver function is triggered after a User instance is saved.
    If the User instance is newly created (created=True),
    it creates a corresponding Profile instance
    associated with the User instance.
    Args:
        sender: The model class that sent the signal (User).
        instance: The actual instance of the model that was saved.
        created: A boolean indicating whether a new record was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)
