# Generated by Django 2.1.5 on 2020-11-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_record', '0012_auto_20201112_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]