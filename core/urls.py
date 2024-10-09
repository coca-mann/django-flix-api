from django.contrib import admin
from django.urls import path
from apps.genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from apps.actors.views import ActorCreatListView, ActorRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    path('actors/', ActorCreatListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]