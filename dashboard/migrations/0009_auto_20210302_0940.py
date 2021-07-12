# Generated by Django 3.1.3 on 2021-03-02 08:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210302_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 2, 8, 39, 48, 29362, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='paymentplan',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
