from django.shortcuts import redirect
from django.urls import reverse


class RedirectToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is logged in
        if request.session.get('is_logged_in'):
            # Get the user's role from the session or wherever it's stored
            user_role = request.session.get('user_role')

            # Redirect to the appropriate dashboard based on the user's role
            if user_role == 1 and request.path == reverse('login_page'):
                return redirect('Admin/homepage')
            elif user_role == 2 and request.path == reverse('login_page'):
                return redirect('Employee/home')

        # Continue with the normal request/response flow
        response = self.get_response(request)
        return response
    
