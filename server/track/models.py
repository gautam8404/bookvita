from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import User
from books.models import Book
from reviews.models import Review

# Create your models here.

STATUS_CHOICES_LIST = ['planning', 'completed', 'reading', 'dropped', 'on-hold']
STATUS_CHOICES = (
    ('planning', 'Planning'),
    ('completed', 'Completed'),
    ('reading', 'Reading'),
    ('dropped', 'Dropped'),
    ('paused', 'Paused'),
)


class Track(models.Model):
    class Meta:
        db_table = 'track'
        ordering = ['date_added']
        unique_together = ('user', 'book')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tracks")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="tracks")
    track_id = models.AutoField(primary_key=True)

    user_rating = models.FloatField(null=True, blank=True, validators=[MinValueValidator(-1), MaxValueValidator(10)],
                                    default=-1)
    date_added = models.DateField(auto_now_add=True)
    date_started = models.DateField(null=True, blank=True)
    date_finished = models.DateField(null=True, blank=True)
    pages_read = models.IntegerField(null=True, blank=True)
    pages_total = models.IntegerField(null=True, blank=True)

    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default=STATUS_CHOICES[0][0])
    reread = models.BooleanField(default=False)
    reread_count = models.IntegerField(default=0)
    increment_reread_count = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.status.lower() not in STATUS_CHOICES_LIST or self.status is None:
            self.status = STATUS_CHOICES[0][0]

        if self.status == 'Completed':
            self.pages_read = self.pages_total
        if self.pages_total and self.pages_read == self.pages_total:
            self.status = 'Completed'

        if self.reread is True:
            self.increment_reread_count = True
        if self.increment_reread_count is True:
            self.reread_count += 1
            self.increment_reread_count = False

        super(Track, self).save(*args, **kwargs)

