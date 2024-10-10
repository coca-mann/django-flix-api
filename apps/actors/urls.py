from django.urls import path
from .views import ActorCreatListView, ActorRetrieveUpdateDestroyView


urlpatterns = [
    path('actors/', ActorCreatListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]