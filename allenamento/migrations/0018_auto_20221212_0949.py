# Generated by Django 2.1.5 on 2022-12-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allenamento', '0017_auto_20221212_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedario',
            name='addominali',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='schedario',
            name='gambe',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='schedario',
            name='spinta',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='schedario',
            name='tirata',
            field=models.IntegerField(default=0),
        ),
    ]
