# Generated by Django 4.1.7 on 2023-02-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclib', '0003_song_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
