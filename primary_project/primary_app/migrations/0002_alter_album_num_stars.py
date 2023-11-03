# Generated by Django 4.1.7 on 2023-10-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Average'), (4, 'Good'), (5, 'Very Good')]),
        ),
    ]