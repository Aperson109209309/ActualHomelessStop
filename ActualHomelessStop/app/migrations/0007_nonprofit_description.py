# Generated by Django 5.1.1 on 2024-09-29 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_nonprofit_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonprofit',
            name='description',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
