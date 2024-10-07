from rest_framework.permissions import BasePermission

class IsStaff(BasePermission):
    """
    Custom permission to only allow access to staff users.
    """
    
    def has_permission(self, request, view):
        """
        Check if the user is authenticated and is a staff member.
        """
        return bool(request.user and request.user.is_staff)