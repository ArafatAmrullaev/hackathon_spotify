from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            request.user.is_staff