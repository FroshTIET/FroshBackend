# Generated by Django 3.1 on 2020-08-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whodunit', '0003_auto_20200818_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]