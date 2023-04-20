# Generated by Django 4.2 on 2023-04-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='track',
            field=models.ManyToManyField(related_name='book_track', to='track.track'),
        ),
    ]