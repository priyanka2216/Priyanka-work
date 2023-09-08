from django.shortcuts import redirect
from django.urls import reverse

class RedirectToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is logged in and redirect to home page if so
        if request.session.get('is_logged_in') and request.path == reverse('login_page'):
            return redirect('Admin/homepage')
        # Redirect to 'Admin/homepage' URL if logged in and trying to access the login page
        response = self.get_response(request)
        return response
