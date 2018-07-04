from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the 'Owner' of this Object "

    def has_obj_permission(self, request, view, obj):
        return obj.owner == request.owner