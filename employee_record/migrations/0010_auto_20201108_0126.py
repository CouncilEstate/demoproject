# Generated by Django 2.1.5 on 2020-11-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_record', '0009_auto_20201108_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employee_ID',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
