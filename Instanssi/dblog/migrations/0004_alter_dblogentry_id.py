# Generated by Django 3.2.2 on 2021-05-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dblog", "0003_auto_20180711_2110"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dblogentry",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
