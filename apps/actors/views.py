from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.actors.models import Actor
from apps.actors.serializers import ActorSerializer
from core.permissions import GlobalDefaultPermission


class ActorCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer