# Generated by Django 3.2.18 on 2023-03-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kompomaatti", "0007_alternateentryfile"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="created_at",
            field=models.DateTimeField(default=None, verbose_name="Luontiaika", null=True),
        ),
    ]
