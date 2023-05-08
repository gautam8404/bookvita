from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .helpers import get_book, get_trending, get_subject, get_search
from .serializers import BookSerializer, BookOLSerializer, BookLessSerializer
from .models import Book, BookLikes
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

    def get_queryset(self):
        return Book.objects.filter(book_id=self.kwargs.get('book_id'))

    def retrieve(self, request, *args, **kwargs):
        if isinstance(self.get_serializer(), BookSerializer):
            return super().retrieve(request, *args, **kwargs)
        else:
            book = get_book(kwargs.get('book_id'))
            serializer = self.get_serializer(book)
            res = serializer.data
            return Response(res)

    def get_serializer_class(self):
        if Book.objects.filter(book_id=self.kwargs.get('book_id')).exists():
            return BookSerializer
        else:
            return BookOLSerializer


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


class BookOLSearch(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        query = self.request.query_params.get('q')
        limit = int(self.request.query_params.get('limit', 0))
        offset = int(self.request.query_params.get('offset', 0))
        books = get_search(query, limit, offset)
        serializer = BookOLSerializer(books['results'], many=True)
        books['results'] = serializer.data
        return Response(books)


class ToggleBookLikesView(APIView):
    http_method_names = ['post']
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        book_id = self.kwargs.get('book_id')
        user = request.user
        if Book.objects.filter(book_id=book_id).exists():
            book = Book.objects.get(book_id=book_id)
            if BookLikes.objects.filter(book=book, user=user).exists():
                BookLikes.objects.filter(book=book, user=user).delete()
                return Response({'message': 'Book removed from likes'})
            else:
                BookLikes.objects.create(book=book, user=user)
                return Response({'message': 'Book added to likes'})
        else:
            return Response({'message': 'Book not found'})


class UserLikesView(APIView):
    http_method_names = ['get']
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        books = BookLikes.objects.filter(user=user)
        bks = []
        for book in books:
            bks.append(book.book)
        serializer = BookLessSerializer(bks, many=True)
        return Response(serializer.data)