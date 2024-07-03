# middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class PreventAdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is an admin and is authenticated
        if request.user.is_authenticated and request.user.is_superuser:
            # Check if the user is accessing the admin login page
            if request.path.startswith(reverse('admin:index')):
                return redirect(reverse('admin:index'))  # Redirect to the admin index page

        return response
