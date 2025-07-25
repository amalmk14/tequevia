# Generated by Django 5.2.4 on 2025-07-24 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_module_service', '0007_productmastervariant_season_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2025, 7, 24, 7, 1, 19, 154878, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='delete_status',
            field=models.BooleanField(default=False),
        ),
    ]
