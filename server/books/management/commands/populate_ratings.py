from django.core.management.base import BaseCommand, CommandError
from books.models import Rating

import json


class Command(BaseCommand):
    help = 'Populate ratings from json file, must not be run more than once'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to json file',
                            default='OLdump/ol_dump_ratings_2023-03-31.json')

    def handle(self, *args, **options):
        path = options['file']
        if not path.endswith('.json'):
            raise CommandError('File must be json')

        with open(path) as f:
            data = json.load(f)
            ratings = []
            for key in data:
                ratings.append(Rating(book_id=key, rating=data[key]))

            Rating.objects.bulk_create(ratings, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS('Successfully populated ratings'))
