from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user

class IsOwner(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.user.is_authenticated:
      if request.user.username != obj.user.username:
        print(request.user)
        return False
      else:
        return True
    else:
      return False

