# Generated by Django 3.1 on 2020-08-17 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0003_score_whodunit_level_coverage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='whodunit_level_coverage',
            new_name='whodunit_level',
        ),
    ]
