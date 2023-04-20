from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers import get_book, get_trending, get_subject
from .serializers import BookSerializer, BookOLSerializer
from .models import Book
from rest_framework import generics


# Create your views here.

class BookListView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'subjects', 'author__name']
    ordering_fields = ['title', 'author__name', 'publish_date', 'average_rating', 'ratings_count']
    http_method_names = ['get', 'post']


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'book_id'
    http_method_names = ['get', 'put', 'delete']

    # def get_queryset(self):
    #     return Book.objects.filter(book_id=self.kwargs.get('book_id'))

    def retrieve(self, request, *args, **kwargs):
        if Book.objects.filter(book_id=kwargs.get('book_id')).exists():
            return super().retrieve(request, *args, **kwargs)
        else:
            print('not in db')
            book = get_book(kwargs.get('book_id'))
            print(book)
            serializer = BookOLSerializer(book)
            return Response(serializer.data)


class BookOLTrending(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        time = self.kwargs.get('time')
        limit = int(self.request.query_params.get('limit', 0))
        page = int(self.request.query_params.get('page', 1))
        books = get_trending(time, limit, page)
        serializer = BookOLSerializer(books['results'], many=True)
        books['results'] = serializer.data
        return Response(books)


class BookOLSubject(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        subject = self.kwargs.get('subject')
        limit = int(self.request.query_params.get('limit', 0))
        offset = int(self.request.query_params.get('offset', 0))
        books = get_subject(subject, limit, offset)
        serializer = BookOLSerializer(books['results'], many=True)
        books['results'] = serializer.data
        return Response(books)
