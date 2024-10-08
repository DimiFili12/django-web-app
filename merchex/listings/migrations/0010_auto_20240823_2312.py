# Generated by Django 3.1.7 on 2024-08-23 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20240823_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('RE', 'Records'), ('CL', 'Clothing'), ('PO', 'Posters'), ('MI', 'Miscellaneous')], default='MI', max_length=2),
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
