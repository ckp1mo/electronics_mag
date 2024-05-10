from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Права доступа. Доступ только активным пользователям и авторизованным."""
    def has_permission(self, request, view):
        return request.user and request.user.is_active
