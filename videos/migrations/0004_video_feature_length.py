# Generated by Django 4.2.9 on 2024-04-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_aspect_ratio_alter_video_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='feature_length',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
