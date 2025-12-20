from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

    # def validate_release_date(self, value):
    #     if value.year < 1990:
    #         raise serializers.ValidationError('A data de lançamento é inferior a 1990!!')
    #     return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O Resumo não pode ser maior que 200 Caracteres.')
        return value