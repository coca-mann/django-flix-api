from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.movies.models import Movie
from apps.movies.serializers import MovieSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer