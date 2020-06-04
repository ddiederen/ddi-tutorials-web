# imports
from rest_framework import permissions

# permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission.
    To only allow owners of an object to edit it, an 'owner' entry is required in the table
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        # return obj.owner == request.user

        # all allowed
        return True
