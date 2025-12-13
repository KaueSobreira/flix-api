import json
from django.http import JsonResponse
from .models import Genre
from  django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def genre_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        genre_list = [
            {
                'id': genre.id,
                'name': genre.name
            }
            for genre in genres
        ]
        return JsonResponse(genre_list, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {
                'id': new_genre.id,
                'name': new_genre.name
            },
            status=201,
        )
