# Generated by Django 3.1.2 on 2020-11-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to='Videos'),
        ),
    ]
