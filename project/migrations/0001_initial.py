# Generated by Django 5.0.7 on 2024-07-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_identification', models.IntegerField(max_length=2)),
                ('stock', models.IntegerField()),
                ('namep', models.CharField(max_length=20)),
            ],
        ),
    ]
