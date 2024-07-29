# Generated by Django 5.0.2 on 2024-03-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameWebsite', '0012_rename_snake_game_3_profile_momory_card_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='car_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='car_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='car_game_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='flappy_bird_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='flappy_bird_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='flappy_bird_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='hangman_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hangman_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='puzzle_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='puzzle_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='puzzle_game_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='rock_paper_scissors_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='rock_paper_scissors_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tic_tac_toe_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tic_tac_toe_2',
            field=models.BooleanField(default=True),
        ),
    ]
