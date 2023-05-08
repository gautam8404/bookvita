import rest_framework.exceptions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from users.models import User
from .models import BookShelves, BookShelveBooks, BookShelveLikes
from .serializers import BookShelveSerializer, BookShelveDetailSerializer, BookShelveModifySerializer
from rest_framework import generics, permissions, status, filters
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class BookShelveALLView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = [JWTAuthentication]
    serializer_class = BookShelveSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'date_created', 'date_updated', 'book_count', 'likes']
    queryset = BookShelves.objects.all()
    http_method_names = ['get']


class BookShelveUserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BookShelveSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'date_created', 'date_updated', 'book_count', 'likes']
    http_method_names = ['get', 'post']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BookShelves.objects.filter(user=user)

    def perform_create(self, serializer):
        print(self.request.user.is_authenticated)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=self.kwargs.get('username'))
        serializer.save(user=user)

    def get_serializer_class(self):
        if self.request.query_params.get('details', None) == 'true':
            return BookShelveDetailSerializer
        return BookShelveSerializer


class BookShelveDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = [JWTAuthentication]
    serializer_class = BookShelveDetailSerializer
    lookup_field = 'bookshelf_id'
    http_method_names = ['get', 'put', 'delete']

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs.get('username'))
        return BookShelves.objects.filter(user=user, bookshelf_id=self.kwargs.get('bookshelf_id'))

    def put(self, *args, **kwargs):
        self.partial_update(*args, **kwargs)
        return Response(status=status.HTTP_200_OK)


class BookShelveModifyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        # return list of bookids in bookshelf
        bookshelf = get_object_or_404(BookShelves, bookshelf_id=kwargs.get('bookshelf_id'))
        book_ids = [book.book_id for book in bookshelf.books.all()]
        return Response(book_ids, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        bookshelf = get_object_or_404(BookShelves, bookshelf_id=kwargs.get('bookshelf_id'))
        book_ids = request.data.get('book_ids')
        print(book_ids)
        if not book_ids:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        for book_id in book_ids:
            if not Book.objects.filter(book_id=book_id).exists():
                from books.helpers import create_book
                try:
                    create_book(book_id)
                except:
                    continue    # if book does not exist in olib, skip it
            book = get_object_or_404(Book, book_id=book_id)
            if not BookShelveBooks.objects.filter(book=book, book_shelve=bookshelf).exists():
                BookShelveBooks.objects.create(book=book, book_shelve=bookshelf)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        bookshelf = get_object_or_404(BookShelves, bookshelf_id=kwargs.get('bookshelf_id'))
        book_ids = request.query_params.get('books')
        book_ids = book_ids.split(',')
        print(book_ids)
        if not book_ids:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        for book_id in book_ids:
            book = get_object_or_404(Book, book_id=book_id)
            if BookShelveBooks.objects.filter(book=book, book_shelve=bookshelf).exists():
                BookShelveBooks.objects.filter(book=book, book_shelve=bookshelf).delete()
        return Response(status=status.HTTP_200_OK)


class ToggleShelfLikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        bookshelf = get_object_or_404(BookShelves, bookshelf_id=kwargs.get('bookshelf_id'))
        if not BookShelveLikes.objects.filter(book_shelve=bookshelf, user=request.user).exists():
            BookShelveLikes.objects.create(book_shelve=bookshelf, user=request.user)
        else:
            BookShelveLikes.objects.filter(book_shelve=bookshelf, user=request.user).delete()
        return Response(status=status.HTTP_200_OK)


# returns list of bookshelves liked by user
class BookShelveLikedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        user = request.user
        bookshelves = BookShelves.objects.filter(book_shelve_likes__user=user)
        serializer = BookShelveSerializer(bookshelves, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)