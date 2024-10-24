from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.actors.models import Actor
from apps.actors.serializers import ActorSerializer


class ActorCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer