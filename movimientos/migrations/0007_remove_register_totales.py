# Generated by Django 4.1.3 on 2023-04-16 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0006_alter_register_totales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='totales',
        ),
    ]
