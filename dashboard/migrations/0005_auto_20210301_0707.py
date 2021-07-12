# Generated by Django 3.1.3 on 2021-03-01 06:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210222_0751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='discount',
            new_name='total_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='final_value',
        ),
        migrations.RemoveField(
            model_name='order',
            name='value',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='company_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='order',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='product_five',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='product_four',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='product_one',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='product_seven',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='product_six',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='product_three',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='product_two',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='telephone',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 1, 6, 7, 40, 616258, tzinfo=utc)),
        ),
    ]