# Generated by Django 5.1.2 on 2025-02-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ends',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='starts',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
