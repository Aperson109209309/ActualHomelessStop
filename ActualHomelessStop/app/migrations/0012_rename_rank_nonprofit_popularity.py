# Generated by Django 5.1.2 on 2024-12-01 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nonprofit',
            old_name='rank',
            new_name='popularity',
        ),
    ]