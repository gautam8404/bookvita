from rest_framework import serializers

from books.models import Book
from track.models import Track
from users.models import User
from .models import ReviewLikes, Review


class ReviewSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user', 'date_added', 'review_id', 'book', 'likes']

    def get_likes(self, obj):
        return ReviewLikes.objects.filter(review=obj).count()


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user', 'date_added', 'review_id', 'book']

    def create(self, validated_data):
        review = Review.objects.create(
            user=User.objects.get(username__exact=self.context['user']),
            book=Book.objects.get(book_id__exact=self.context['book_id']),
            review=validated_data['review']
        )
        return review

    def validate(self, attrs):
        user = User.objects.get(username__exact=self.context['user'])
        book_id = self.context['book_id']
        if not Track.objects.filter(user=user, book=book_id).exists():
            raise serializers.ValidationError({"code": "not_in_library"
                                               , "message": "You must have this book in your library to review it."})
        return attrs

