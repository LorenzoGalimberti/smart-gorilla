# Generated by Django 2.1.5 on 2022-12-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allenamento', '0032_auto_20221213_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocco',
            name='duration',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
