# Generated by Django 5.1.1 on 2024-09-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_nonprofit_donation_link_nonprofit_newspaper_signup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonprofit',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
