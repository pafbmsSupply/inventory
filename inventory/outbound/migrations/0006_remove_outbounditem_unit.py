# Generated by Django 5.0.7 on 2024-08-03 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outbound', '0005_outbounditem_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outbounditem',
            name='unit',
        ),
    ]
