# Generated by Django 4.2.6 on 2023-10-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]