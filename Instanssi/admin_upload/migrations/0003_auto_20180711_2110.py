# Generated by Django 2.0.7 on 2018-07-11 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_upload", "0002_auto_20180711_2054"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedfile",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="kompomaatti.Event",
                verbose_name="Tapahtuma",
            ),
        ),
    ]
