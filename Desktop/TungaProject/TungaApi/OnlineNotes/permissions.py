from rest_framework import permissions

#Implementing IsOwnerOrReadOnly permission logic
class IsOwnerOrReadOnly(permissions.BasePermission):