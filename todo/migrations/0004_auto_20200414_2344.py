# Generated by Django 3.0.3 on 2020-04-14 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200414_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
