# Generated by Django 4.0 on 2021-12-15 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0003_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
