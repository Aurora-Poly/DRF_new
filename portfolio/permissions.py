from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.user.is_authenticated:
      if request.user != obj.user:
        return False
      else:
        return True
    else:
      return False
