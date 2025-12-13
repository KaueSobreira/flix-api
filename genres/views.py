import json
from django.http import JsonResponse
from .models import Genre
from  django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.
@csrf_exempt
def genre_create_list_view(request):
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

@csrf_exempt
def genre_detail_update_delete_view(request, id):
    genre = get_object_or_404(Genre, pk=id)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {
                'message': 'Genero atualizado com Sucesso',
                'id': genre.id,
                'name': genre.name
            },
            status=201,
        )
    
    elif request.method == 'DELETE':
        genre.delete()

        return JsonResponse(
            {
                'message': 'Genero Deletado com Sucesso',
            },
            status=204,
        )