# Generated by Django 3.1.7 on 2024-08-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_listing_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
