# Generated by Django 3.0.8 on 2020-09-29 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0004_auto_20200929_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='final',
            name='country',
        ),
        migrations.AddField(
            model_name='final',
            name='country',
            field=models.ForeignKey(default='India', on_delete=django.db.models.deletion.SET_DEFAULT, to='country.countries'),
        ),
        migrations.RemoveField(
            model_name='final',
            name='disaster',
        ),
        migrations.AddField(
            model_name='final',
            name='disaster',
            field=models.ForeignKey(default='Tsunami', on_delete=django.db.models.deletion.SET_DEFAULT, to='country.disaster'),
        ),
    ]
