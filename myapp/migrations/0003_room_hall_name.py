# Generated by Django 5.1.2 on 2024-11-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='hall_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
