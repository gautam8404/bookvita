from rest_framework import serializers
from .models import Track
from books.models import Book


class TrackSerializer(serializers.ModelSerializer):
    book_id = serializers.CharField()

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ['user', 'date_added', 'track_id', 'review', 'increment_reread_count', 'reread_count',
                            'book']

    def validate_book(self, book_id):
        try:
            print("book_id", book_id)
            book = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            print("here")
            from books.serializers import BookSerializer
            serializer = BookSerializer(data={'book_id': book_id})
            if serializer.is_valid():
                book = serializer.save()
            else:
                raise serializers.ValidationError({'code': 'book_does_not_exist', 'message': 'Book does not exist.'})
        return book

    def validate_track(self, user, book):
        if Track.objects.filter(user=user, book=book).exists():
            raise serializers.ValidationError({'code': 'book_already_in_library', 'message': 'Book already in library.'})

    def validate(self, data):
        book_id = data['book_id']
        book = self.validate_book(book_id)
        data['book'] = book

        user = self.context['request'].user
        self.validate_track(user, book)

        validated_data = super().validate(data)
        return validated_data


class TrackBookDetailSerializer(TrackSerializer):
    book = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ['user', 'date_added', 'track_id', 'review', 'increment_reread_count', 'reread_count']

    def get_book(self, obj):
        from books.serializers import BookSerializer
        return BookSerializer(obj.book).data