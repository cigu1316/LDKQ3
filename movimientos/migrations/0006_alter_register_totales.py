# Generated by Django 4.1.3 on 2023-04-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0005_alter_register_totales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='totales',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
    ]
