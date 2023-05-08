import django_filters
from rest_framework import generics, filters, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from users.models import User
from track.models import Track

from .serializers import ReviewSerializer, ReviewCreateSerializer
from .models import Review, ReviewLikes


# Create your views here.

# class UserFilter(django_filters.FilterSet):
#     username = django_filters.CharFilter(lookup_expr='iexact')
#
#     class Meta:
#         model = User
#         fields = ['username']


class ReviewFilter(django_filters.FilterSet):
    book = django_filters.CharFilter(lookup_expr='exact')
    user = django_filters.CharFilter(field_name='user__username', lookup_expr='exact')
    like = django_filters.BooleanFilter(field_name='likes', lookup_expr='isnull', exclude=True)

    # user_filter = UserFilter

    class Meta:
        model = Review
        fields = ['user', 'book']
        ordering = ['-likes']

    order_by = django_filters.OrderingFilter(
        fields=(
            ('book__title', 'title'),
            ('book__author', 'author'),
            ('book__published_date', 'published_date'),
            ('date_added', 'date_added'),
            ('user__user_rating', 'user_rating'),
            ('likes', 'likes'),
        ),
    )

    # def filter_user(self, queryset, name, value):
    #     return queryset.filter(user__username=value)


class ReviewListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ReviewFilter
    # ordering_fields = ['likes']
    http_method_names = ['get']
    ordering = ['-likes']


class ReviewCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReviewCreateSerializer
    authentication_classes = [JWTAuthentication]
    http_method_names = ['post']

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        context['book_id'] = self.kwargs.get('book_id')
        return context


class ReviewRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get', 'put', 'delete']
    lookup_field = 'review_id'

    def get_queryset(self):
        return Review.objects.filter(review_id__exact=self.kwargs.get('review_id'))

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ToggleLikeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        print(self.kwargs.get('review_id'))
        review = get_object_or_404(Review, review_id=self.kwargs.get('review_id'))
        user = request.user
        if ReviewLikes.objects.filter(review=review, user=user).exists():
            ReviewLikes.objects.filter(review=review, user=user).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            ReviewLikes.objects.create(review=review, user=user)
            return Response(status=status.HTTP_201_CREATED)
