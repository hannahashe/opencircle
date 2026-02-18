from django.contrib import admin
from .models import Event, Profile, Notification


admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Notification)