# Generated by Django 4.2.9 on 2024-04-23 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0009_video_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='rating',
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_rating', to='videos.video')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
