# Generated by Django 4.2.3 on 2023-07-13 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("musafar", "0003_remove_song_audio_link_remove_song_duration"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Datas",
        ),
    ]
