from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer