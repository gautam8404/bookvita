from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from users.models import User
from .serializers import TrackSerializer, TrackBookDetailSerializer
from rest_framework import generics, filters, status
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Track


# Create your views here.

class TrackView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Track.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['book__book_id', 'favorite', 'status']
    # search_fields = ['book__title', 'book__author']
    ordering_fields = ['book__title', 'book__author', 'book__published_date', 'date_added', 'user_rating']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Track.objects.filter(user=user)

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

    def get_serializer_class(self):
        # details in book params
        if self.request.query_params.get('details', None) == 'true':
            return TrackBookDetailSerializer
        return TrackSerializer


class TrackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrackSerializer
    lookup_field = 'book_id'
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'delete']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Track.objects.filter(user=user, book=self.kwargs.get('book_id'))

    def put(self, *args, **kwargs):
        self.partial_update(*args, **kwargs)
        return Response(status=status.HTTP_200_OK)

    def get_serializer_class(self):
        # details in book params
        if self.request.query_params.get('details', None) == 'true':
            return TrackBookDetailSerializer
        return TrackSerializer
