# Generated by Django 3.1.2 on 2020-11-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videoapp', '0002_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='uploaded_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
