# Generated by Django 4.2 on 2023-04-29 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookShelveBooks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'book_shelve_books',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='BookShelveLikes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'book_shelve_likes',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='BookShelves',
            fields=[
                ('bookshelf_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('books', models.ManyToManyField(related_name='book_shelves', through='bookshelves.BookShelveBooks', to='books.book')),
            ],
            options={
                'db_table': 'book_shelve',
                'ordering': ['name'],
            },
        ),
    ]
