# Generated by Django 3.0.8 on 2020-09-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0003_final_disaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='final',
            name='Lattitude',
            field=models.CharField(default='lattitude', max_length=100),
        ),
        migrations.AlterField(
            model_name='final',
            name='Longitude',
            field=models.CharField(default='longitude', max_length=100),
        ),
    ]
