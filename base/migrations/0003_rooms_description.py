# Generated by Django 3.2.9 on 2021-11-18 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
