# Generated by Django 5.0 on 2023-12-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gaanaapp', '0003_remove_singer_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='lang',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
