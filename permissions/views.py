from django.contrib.auth.models import Permission
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from .serializers import PermissionSerializer


class PermissionListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
