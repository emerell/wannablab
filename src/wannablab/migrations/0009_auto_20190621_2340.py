# Generated by Django 2.2.1 on 2019-06-21 20:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wannablab', '0008_auto_20190621_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='event_member', to=settings.AUTH_USER_MODEL, verbose_name='Members'),
        ),
    ]