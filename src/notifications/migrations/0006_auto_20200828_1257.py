# Generated by Django 3.1 on 2020-08-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0005_auto_20200828_1255"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timelineevent",
            name="color",
            field=models.CharField(default="0xFF40C752", max_length=128),
        ),
    ]