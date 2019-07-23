# Generated by Django 2.2.1 on 2019-07-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wannablab', '0013_auto_20190723_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.RemoveField(
            model_name='language',
            name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Name'),
        ),
    ]
