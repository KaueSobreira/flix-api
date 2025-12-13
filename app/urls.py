from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, genre_detail_update_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:id>', genre_detail_update_delete_view, name='genre-detail-update-delete-list'),
]
