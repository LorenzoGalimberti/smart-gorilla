# Generated by Django 2.1.5 on 2022-12-14 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('allenamento', '0033_auto_20221213_1029'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=120)),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('autore_descrizione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussione', to=settings.AUTH_USER_MODEL)),
                ('scheda_appartenenza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allenamento.Schedario')),
            ],
            options={
                'verbose_name': 'Discussione',
                'verbose_name_plural': 'Discussioni',
            },
        ),
    ]
