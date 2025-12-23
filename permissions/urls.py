from django.urls import path
from . import views

urlpatterns = [
    path('permission/', views.PermissionListView.as_view(), name='permission-list-view'),
]
