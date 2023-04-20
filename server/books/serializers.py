from rest_framework import serializers
from .models import Book, Author
from .helpers import create_book, create_authors, get_book

"""
book model fields: book_id, title, published_date, description, cover_url, subjects, language, isbn_10, isbn_13, author
author model fields: author_id, name, author_url, author_info, author_image (url)
"""


class BookLessSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'book_id', 'title', 'publish_date', 'description', 'cover_id', 'authors', 'rating_count', 'average_rating')
        read_only_fields = fields

    def get_authors(self, obj):
        authors = obj.author.all()
        return AuthorSerializer(authors, many=True).data


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    subjects = serializers.ListField(child=serializers.CharField(), required=False, read_only=True)

    class Meta:
        model = Book
        fields = ('book_id', 'title', 'publish_date', 'description', 'cover_id', 'subjects', 'authors', 'rating_count',
                  'average_rating')
        read_only_fields = (
            'title', 'publish_date', 'description', 'cover_id', 'subjects', 'authors', 'rating_count', 'average_rating')

    def create(self, validated_data):
        book = create_book(validated_data['book_id'])

        return book

    def get_authors(self, obj):
        authors = obj.author.all()

        return AuthorSerializer(authors, many=True).data


# BookOLSerializer, used when book is not in database to get data from OpenLibrary
class BookOLSerializer(serializers.Serializer):
    book_id = serializers.CharField()
    title = serializers.CharField()
    authors = serializers.ListField(required=False)
    publish_date = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    cover_id = serializers.IntegerField(required=False)
    subjects = serializers.ListField(child=serializers.CharField() ,required=False)

    def create(self, validated_data):
        book = get_book(validated_data['book_id'])

        return book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'name', 'author_url', 'author_info', 'author_image_id')
        read_only_fields = ('author_id', 'name', 'author_url', 'author_info', 'author_image_id')

    def create(self, validated_data):
        authors = create_authors(validated_data)
        return authors
