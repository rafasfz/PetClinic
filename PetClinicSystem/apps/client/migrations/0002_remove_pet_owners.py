# Generated by Django 4.1.1 on 2022-10-02 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='owners',
        ),
    ]
