# Generated by Django 5.1.3 on 2025-03-20 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_alter_booking_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
