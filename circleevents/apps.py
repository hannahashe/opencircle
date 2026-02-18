from django.apps import AppConfig


class CircleeventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "circleevents"

    def ready(self):
        import circleevents.signals
    # This will ensure the signal handlers are connected when the app is ready