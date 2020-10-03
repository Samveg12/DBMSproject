# Generated by Django 3.1 on 2020-10-02 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0009_auto_20201002_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.countries')),
            ],
        ),
    ]