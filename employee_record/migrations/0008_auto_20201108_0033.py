# Generated by Django 2.1.5 on 2020-11-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_record', '0007_auto_20201107_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='emergency',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='telephone',
            field=models.IntegerField(blank=True),
        ),
    ]
