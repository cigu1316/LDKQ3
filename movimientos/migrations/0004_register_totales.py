# Generated by Django 4.1.3 on 2023-04-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0003_alter_register_balance_alter_register_descriptions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='totales',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
    ]