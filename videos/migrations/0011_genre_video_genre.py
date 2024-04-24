# Generated by Django 4.2.9 on 2024-04-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_remove_video_rating_userrating_video_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='genre',
            field=models.ManyToManyField(blank=True, to='videos.genre'),
        ),
    ]
