from django.core import signals
from django.db.models.signals import pre_save

from django.dispatch import receiver

from books.models import Book


@receiver(pre_save, sender=Book)
def remove_long_subjects(sender, instance, **kwargs):
    if instance.subjects:
        subs = []
        for sub in instance.subjects:
            s = sub.split()
            if ":" in sub:
                continue
            subs.append(sub)
        instance.subjects = subs
