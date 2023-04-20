from rest_framework import serializers
from .models import BookShelves, BookShelveBooks, BookShelveLikes
from books.serializers import BookLessSerializer


class BookShelveBooksSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()

    class Meta:
        model = BookShelveBooks
        fields = '__all__'
        read_only_fields = ['book', 'book_shelve']

    def get_book(self, obj):
        return BookLessSerializer(obj).data


class BookShelveSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    book_count = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BookShelves
        fields = '__all__'
        read_only_fields = ['user', 'books', 'likes']

    def get_likes(self, obj):
        return BookShelveLikes.objects.filter(book_shelve=obj).count()

    def get_book_count(self, obj):
        return BookShelveBooks.objects.filter(book_shelve=obj).count()


class BookShelveDetailSerializer(BookShelveSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = BookShelves
        fields = '__all__'
        read_only_fields = ['user', 'books', 'likes']

    def get_books(self, obj):
        print(obj)
        return BookLessSerializer(obj.books.all(), many=True).data


class BookShelveModifySerializer(serializers.Serializer):
    book_ids = serializers.ListField(child=serializers.CharField(), write_only=True)
