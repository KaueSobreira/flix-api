from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        reviews = obj.reviews.all()

        if reviews:
            sum_reviews = 0

            for review in reviews:
                sum_reviews += review.stars

            media = (sum_reviews / len(reviews))

            return round(media, 1)

        return "Esse filme não tem avaliação"

    # def validate_release_date(self, value):
    #     if value.year < 1900:
    #         raise serializers.ValidationError('A data de lançamento é inferior a 1990!!')
    #     return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O Resumo não pode ser maior que 200 Caracteres.')
        return value