# Generated by Django 3.1.7 on 2021-07-06 22:34

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Videoapp', '0015_commment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
