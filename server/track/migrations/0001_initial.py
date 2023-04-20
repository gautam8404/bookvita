# Generated by Django 4.2 on 2023-04-20 19:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_rating', models.FloatField(blank=True, default=-1, null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(10)])),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_finished', models.DateField(blank=True, null=True)),
                ('pages_read', models.IntegerField(blank=True, null=True)),
                ('pages_total', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('completed', 'Completed'), ('reading', 'Reading'), ('dropped', 'Dropped'), ('paused', 'Paused')], default='planning', max_length=20)),
                ('reread', models.BooleanField(default=False)),
                ('reread_count', models.IntegerField(default=0)),
                ('increment_reread_count', models.BooleanField(default=False)),
                ('favorite', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='books.book')),
            ],
            options={
                'db_table': 'track',
                'ordering': ['date_added'],
            },
        ),
    ]