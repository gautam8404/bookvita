from django.db import models
import uuid


# Create your models here.
class Review(models.Model):
    class Meta:
        db_table = 'review'
        ordering = ['created_at']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField(max_length=4000, null=True, blank=True)

    def __str__(self):
        return self.review


class ReviewLikes(models.Model):
    class Meta:
        db_table = 'review_likes'
        ordering = ['created_at']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    review_like_id = models.AutoField(primary_key=True)
    review = models.ForeignKey('reviews.Review', on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="review_likes")

    def __str__(self):
        return self.user.username