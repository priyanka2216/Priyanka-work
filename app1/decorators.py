from functools import wraps
from django.shortcuts import redirect

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is logged in and has the admin role
        if request.user.is_authenticated and request.user.user_type == '1':
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to a different page or handle as needed
            return redirect('login_page')  # You can change this to the appropriate URL

    return _wrapped_view

