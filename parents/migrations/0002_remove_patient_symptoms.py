# Generated by Django 3.1 on 2020-10-13 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='symptoms',
        ),
    ]
