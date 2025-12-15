from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class meta:
        model = Movie
        fields = '__all__'