# Generated by Django 3.1 on 2020-10-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0008_auto_20201002_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finaltable',
            name='enddate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='finaltable',
            name='startdate',
            field=models.DateTimeField(null=True),
        ),
    ]
