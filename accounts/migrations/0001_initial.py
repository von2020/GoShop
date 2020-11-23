# Generated by Django 3.1.2 on 2020-11-17 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(default='', max_length=255, unique=True, verbose_name='email address')),
                ('firstname', models.CharField(default='', max_length=200)),
                ('lastname', models.CharField(default='', max_length=200)),
                ('phone_number', models.IntegerField(default=0)),
                ('work_address', models.CharField(default='', max_length=200)),
                ('salary', models.IntegerField(default=0)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='emp_name')),
                ('short_name', models.CharField(max_length=20, verbose_name='emp_short_name')),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]