from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UsersCreateListView.as_view(), name='users-create-list-view'),
    path('users/<int:pk>', views.UsersUpdateDestroyListView.as_view(), name='users-update-destroy-list-view'),
]