# Generated by Django 4.2.9 on 2024-04-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_video_feature_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='release_year',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4),
        ),
    ]
