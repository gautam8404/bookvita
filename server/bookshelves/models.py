from django.db import models
from users.models import User
from books.models import Book


# Create your models here.

class BookShelveBooks(models.Model):
    class Meta:
        db_table = 'book_shelve_books'
        ordering = ['date_added']

    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_shelve_books")
    book_shelve = models.ForeignKey('BookShelves', on_delete=models.CASCADE, related_name="book_shelve_books")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_shelve.name


class BookShelves(models.Model):
    class Meta:
        db_table = 'book_shelve'
        ordering = ['name']

    bookshelf_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_shelves")
    books = models.ManyToManyField(Book, through='BookShelveBooks', related_name="book_shelves")

    def __str__(self):
        return self.name


class BookShelveLikes(models.Model):
    class Meta:
        db_table = 'book_shelve_likes'
        ordering = ['date_added']

    id = models.AutoField(primary_key=True)
    book_shelve = models.ForeignKey(BookShelves, on_delete=models.CASCADE, related_name="book_shelve_likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_shelve_likes")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_shelve.name + " - " + self.user.username
