# Generated by Django 2.1.5 on 2022-12-12 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allenamento', '0024_schedario_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedario',
            name='slug',
        ),
    ]