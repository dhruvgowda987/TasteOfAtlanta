# Generated by Django 5.0.6 on 2024-06-30 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_favorite_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='place_id',
            field=models.TextField(default='default_place_id'),
        ),
    ]