from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import datetime


# Create your models here.

class Book(models.Model):
    class Meta:
        db_table = 'book'
        ordering = ['title']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    book_id = models.CharField(unique=True, max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    publish_date = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    cover_id = models.IntegerField(null=True, blank=True)
    subjects = ArrayField(models.CharField(max_length=512), null=True, blank=True)

    author = models.ManyToManyField('Author', related_name="book_author")
    track = models.ManyToManyField('track.Track', related_name="book_track")

    rating_count = models.IntegerField(default=0, null=True, blank=True)
    average_rating = models.FloatField(default=0.0, null=True, blank=True)
    book_ol_rating = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_subjects(self):
        return self.subjects


class Author(models.Model):
    class Meta:
        db_table = 'author'
        ordering = ['name']

    name = models.CharField(max_length=255)
    author_id = models.CharField(unique=True, max_length=100, primary_key=True)
    author_url = models.CharField(max_length=255, null=True, blank=True)
    author_info = models.TextField(max_length=2000, null=True, blank=True)
    author_image_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class BookLikes(models.Model):
    class Meta:
        db_table = 'book_likes'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    """
    Rating model

    rating models will be populated by open library's rating dump and will only be used to fetch ratings as long as a
    application don't have enough ratings to calculate its own rating.
    """

    class Meta:
        db_table = 'rating'

    book_id = models.CharField(max_length=100, primary_key=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
