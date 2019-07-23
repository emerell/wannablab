# Generated by Django 2.2.1 on 2019-07-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wannablab', '0015_auto_20190723_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='name',
        ),
        migrations.AddField(
            model_name='level',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, unique=True, verbose_name='Full name'),
        ),
        migrations.AddField(
            model_name='level',
            name='shot_name',
            field=models.CharField(blank=True, max_length=2, unique=True, verbose_name='Shot name'),
        ),
    ]
