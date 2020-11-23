# Generated by Django 3.1.2 on 2020-11-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(default='', max_length=255, unique=True, verbose_name='email address')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_sent'],
            },
        ),
    ]