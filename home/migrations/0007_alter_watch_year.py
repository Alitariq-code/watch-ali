# Generated by Django 4.2.7 on 2023-11-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_alter_watch_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watch",
            name="year",
            field=models.IntegerField(default=None, null=True),
        ),
    ]