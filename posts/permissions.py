from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        # Read only permiisions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the author of a post
        return object.author == request.user
