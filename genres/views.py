from django.http import JsonResponse
from .models import Genre

# Create your views here.
def genre_view(request):
    genres = Genre.objects.all()
    genre_list = [
        {
            'id': genre.id,
            'name': genre.name
        }
        for genre in genres
    ]
    return JsonResponse(genre_list, safe=False)