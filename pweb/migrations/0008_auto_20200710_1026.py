# Generated by Django 3.0.6 on 2020-07-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pweb', '0007_auto_20200710_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='dob',
            field=models.DateTimeField(default='YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'),
        ),
        migrations.AlterField(
            model_name='image',
            name='dob',
            field=models.DateTimeField(default='YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'),
        ),
    ]
