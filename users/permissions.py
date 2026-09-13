
from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'Admin'
        )


class IsAttendantUser(BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role in ["Admin", "Attendant"]
        )
