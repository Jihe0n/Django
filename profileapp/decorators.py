from profileapp.models import Profile
from django.http import*


def profile_ownership(func):

    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated