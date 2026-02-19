
from rest_framework.permissions import  BasePermission

class UniqueApiPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
