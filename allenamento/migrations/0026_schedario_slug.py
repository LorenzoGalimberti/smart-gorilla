# Generated by Django 2.1.5 on 2022-12-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allenamento', '0025_remove_schedario_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedario',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
