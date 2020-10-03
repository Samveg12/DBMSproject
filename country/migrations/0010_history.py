# Generated by Django 3.1 on 2020-10-03 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0009_auto_20201002_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lattitud', models.DecimalField(blank=True, decimal_places=4, default=22.35, max_digits=19, null=True)),
                ('Longitud', models.DecimalField(blank=True, decimal_places=4, default=33.55, max_digits=19, null=True)),
                ('severity', models.CharField(max_length=100, null=True)),
                ('startdate', models.DateTimeField(null=True)),
                ('enddate', models.DateTimeField(null=True)),
                ('city', models.CharField(default='Mumbai', max_length=100)),
                ('radius', models.IntegerField(default=0)),
                ('additionInfo', models.TextField()),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.countries')),
                ('disaster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.disaster')),
            ],
        ),
    ]