# Generated by Django 3.2.5 on 2021-08-13 04:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
