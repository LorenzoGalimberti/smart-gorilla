# Generated by Django 2.1.5 on 2022-12-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allenamento', '0027_esercizio_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocco',
            name='set',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
