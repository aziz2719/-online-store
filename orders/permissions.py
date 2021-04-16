from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProductUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return obj == request.user
