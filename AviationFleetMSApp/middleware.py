from django.shortcuts import HttpResponse


class RoleRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Your role required middleware logic here
        response = self.get_response(request)
        return response


def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated and (request.user.is_superuser or request.user.role in allowed_roles):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You don't have permission to view this page.")

        return wrap if callable(view_func) else wrap(view_func)

    return decorator


def permission_required(permission):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.has_perm(permission):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You don't have permission to view this page.")
        return wrap
    return decorator
