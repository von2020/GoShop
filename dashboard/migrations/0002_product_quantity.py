# Generated by Django 3.1.3 on 2021-02-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
