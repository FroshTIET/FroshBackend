# Generated by Django 3.1 on 2020-08-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whodunit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='current_points',
            field=models.IntegerField(default=100),
        ),
    ]