# Generated by Django 5.0.2 on 2024-03-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameWebsite', '0002_profile_delete_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_game_coin',
            field=models.PositiveIntegerField(default=0),
        ),
    ]