# Generated by Django 3.1.2 on 2020-12-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videoapp', '0004_auto_20201201_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='URL',
            field=models.FilePathField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to='Videos'),
        ),
    ]