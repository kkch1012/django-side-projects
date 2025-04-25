from django.http import HttpResponseForbidden


def role_required(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("로그인이 필요합니다.")

            role_order = {
                "normal": 0,
                "premium": 1,
                "admin": 2,
            }

            user_role = getattr(request.user, "role", "normal")
            if role_order.get(user_role, 0) < role_order[required_role]:
                return HttpResponseForbidden(f"{required_role} 이상 등급만 접근 가능합니다.")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
