# Generated by Django 4.2.6 on 2023-10-19 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
        migrations.RemoveField(
            model_name='video',
            name='videofile',
        ),
        migrations.AddField(
            model_name='video',
            name='caption',
            field=models.CharField(default='some video', max_length=100),
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(default='default_video.mp4', upload_to='video/%y'),
        ),
    ]
