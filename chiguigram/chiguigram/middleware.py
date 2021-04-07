""" Middleware Catalog"""

# Django Imports
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """
    Ensure every user using the platform has all his profile data complete
    Including profile picture, bio, phone number, etc.
    """

    def __init__(self, get_response):
        # Middleware Initialization
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before de view is called

        if not request.user.is_anonymous:
            if not request.user.is_staff:
                if request.path not in [reverse('users:update_profile'),
                                        reverse('users:logout')]:  # If i'm not already in that link
                    # calling a OneToOneField
                    profile = request.user.profile
                    if not profile.profile_picture or not profile.biography:
                        return redirect('users:update_profile')
        else:
            if request.path not in ['admin/', reverse('users:login'), reverse('users:singup')]:  # If i'm not already
                # in that
                # link
                return redirect('users:login')
        response = self.get_response(request)
        return response
