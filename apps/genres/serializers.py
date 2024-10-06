from rest_framework import serializers
from apps.genres.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'