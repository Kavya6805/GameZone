# Generated by Django 5.0.2 on 2024-03-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameWebsite', '0013_profile_car_1_profile_car_2_profile_car_game_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='purchase_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='purchase_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='purchase_3',
            field=models.BooleanField(default=False),
        ),
    ]
