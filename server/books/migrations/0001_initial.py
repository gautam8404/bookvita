# Generated by Django 4.2 on 2023-04-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('author_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('author_url', models.CharField(blank=True, max_length=255, null=True)),
                ('author_info', models.TextField(blank=True, max_length=2000, null=True)),
                ('author_image_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'author',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('cover_id', models.IntegerField(blank=True, null=True)),
                ('subjects', models.TextField(blank=True, null=True)),
                ('rating_count', models.IntegerField(blank=True, default=0, null=True)),
                ('average_rating', models.FloatField(blank=True, default=0.0, null=True)),
                ('author', models.ManyToManyField(related_name='book_author', to='books.author')),
            ],
            options={
                'db_table': 'book',
                'ordering': ['title'],
            },
        ),
    ]