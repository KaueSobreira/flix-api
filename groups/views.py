from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from .serializers import GroupSerializer


class GroupCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupRetrieveDestroyUpdateListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
