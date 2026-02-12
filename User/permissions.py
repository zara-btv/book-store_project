
from rest_framework.permissions import  BasePermission




class HasBluePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('ColorBook.Blue')