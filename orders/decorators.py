from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def role_required(roles:list):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # 1. Ensure the user is logged in
            if not request.user.is_authenticated:
                return redirect('login_view_url')
            
            # 2. Check if the user's role matches the required role
            if request.user.role not in roles:
                raise PermissionDenied("Access denied.")
            
            # 3. Fail if they don't have the role
            return view_func(request, *args, **kwargs)
            
        return _wrapped_view
    return decorator
