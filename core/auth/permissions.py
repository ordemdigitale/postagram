from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS

        if view.basename in ["post"]:
            return bool(request.user and request.user.is_authenticated)

        if view.basename in ["post-comment"]:
            if request.method in ["DELETE"]:
                return bool(request.user.is_superuser or request.user in [obj.author, obj.post.author])

            return bool(request.user and request.user.is_authenticated)
    
    def has_permission(self, request, view):
        if view.basename in ["post"]:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS

            return bool(request.user and request.user.is_authenticated)

        return False