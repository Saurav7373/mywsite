# Generated by Django 3.0.6 on 2020-07-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pweb', '0027_image_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='province',
            field=models.CharField(max_length=50),
        ),
    ]