# Generated by Django 3.1.6 on 2022-06-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='company',
            field=models.CharField(max_length=100),
        ),
    ]
