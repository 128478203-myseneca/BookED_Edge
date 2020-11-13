from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the owner of the post to edit it !"

    def has_object_permission(self, request, view, obj):
        safe_methods = ["PUT"]
        if request.method == safe_methods:
            return True
        return obj.author == request.user
