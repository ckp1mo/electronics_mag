from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Разрешение. Доступ только активным пользователям и авторизованным."""
    def has_permission(self, request, view):
        return request.user and request.user.is_active
