from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from .models import Track


@receiver(post_save, sender=Track)
def update_book_rating(sender, instance, **kwargs):
    book = instance.book
    rating_count = Track.objects.filter(book=book).exclude(user_rating=-1).count()
    rating = Track.objects.filter(book=book).exclude(user_rating=-1).aggregate(Avg('user_rating'))['user_rating__avg']
    book.average_rating = rating if rating else 0
    book.rating_count = rating_count if rating_count else 0
    book.save()
