# Generated by Django 2.2.1 on 2019-06-01 15:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Title')),
                ('level', models.CharField(choices=[('A1', 'Beginner'), ('A2', 'Elementary'), ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], default='A1', max_length=2, verbose_name='Level')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('topic', models.CharField(max_length=150, verbose_name='Topic')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('max_members', models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(50)], verbose_name='Max number of members')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Category')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language', to=settings.AUTH_USER_MODEL, verbose_name='Language')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_member', to=settings.AUTH_USER_MODEL, verbose_name='Member')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('text', models.TextField(verbose_name='Text')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Recipient')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comment',
            },
        ),
    ]
