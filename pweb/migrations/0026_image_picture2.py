# Generated by Django 3.0.6 on 2020-07-12 08:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pweb', '0025_auto_20200712_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='picture2',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='palmpic'),
            preserve_default=False,
        ),
    ]
