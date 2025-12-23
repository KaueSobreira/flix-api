from django.urls import path
from . import views


urlpatterns = [
    path('groups/', views.GroupCreateListView.as_view(), name='group-create-list-view'),

    path('groups/<int:pk>/', views.GroupRetrieveDestroyUpdateListView.as_view(), name='group-retrieve-destroy-list-view'),
]
