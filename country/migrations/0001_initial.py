# Generated by Django 3.1 on 2020-09-30 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='enter', max_length=100)),
                ('image', models.ImageField(upload_to='country/images')),
            ],
        ),
        migrations.CreateModel(
            name='disaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='enter', max_length=100)),
                ('image', models.ImageField(upload_to='country/images')),
                ('precautions', models.TextField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='safehaven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='enter', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='enter', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='finalTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lattitude', models.CharField(default='lattitude', max_length=100, null=True)),
                ('Longitude', models.CharField(default='longitude', max_length=100, null=True)),
                ('severity', models.CharField(max_length=100, null=True)),
                ('startdate', models.DateField(null=True)),
                ('enddate', models.DateField(null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.countries')),
                ('disaster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.disaster')),
                ('safehaven', models.ManyToManyField(to='country.safehaven')),
                ('transport', models.ManyToManyField(to='country.transport')),
            ],
        ),
    ]