# Generated by Django 4.1.1 on 2022-10-03 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='diagnosis',
            field=models.TextField(default='', verbose_name='Diagnóstico'),
            preserve_default=False,
        ),
    ]
