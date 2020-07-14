# Generated by Django 3.0.6 on 2020-07-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pweb', '0009_auto_20200710_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=14)),
                ('dob', models.DateTimeField(default='')),
                ('district', models.CharField(max_length=50)),
                ('province', models.CharField(default='', max_length=50)),
                ('desc', models.TextField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Client0',
        ),
    ]
