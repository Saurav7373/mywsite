# Generated by Django 3.0.6 on 2020-07-10 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pweb', '0004_auto_20200710_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='image',
            name='dou1',
        ),
    ]