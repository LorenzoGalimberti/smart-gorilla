# Generated by Django 2.1.5 on 2022-12-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allenamento', '0028_auto_20221213_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocco',
            name='reps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blocco',
            name='zavorra',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
