# Generated by Django 5.1.2 on 2024-12-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_room_hall_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'ordering': ['facility_name']},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-payment_date']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['room_name']},
        ),
        migrations.AlterModelOptions(
            name='roomfacility',
            options={'ordering': ['room', 'facility']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='payment',
            name='mpesa_transaction_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('mpesa', 'M-Pesa'), ('credit_card', 'Credit Card'), ('cash', 'Cash'), ('bank_transfer', 'Bank Transfer'), ('paypal', 'PayPal')], default='mpesa', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_username', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('canceled', 'Canceled')], db_index=True, default='pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='facility',
            name='facility_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('room', 'start_date', 'end_date')},
        ),
    ]
