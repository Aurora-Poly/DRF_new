# Generated by Django 3.1.6 on 2022-06-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='detail',
            field=models.TextField(),
        ),
    ]
