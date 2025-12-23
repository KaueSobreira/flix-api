from django.contrib.auth.models import User
from app.permissions import GlobalDefaultPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UserSerializer


class UsersCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersUpdateDestroyListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
