from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def organiser_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.profile.is_organiser:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return _wrapped_view
