# Generated by Django 3.1.6 on 2022-06-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20220608_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='likes',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='portfolio/file/{author}/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='head_img',
            field=models.ImageField(blank=True, upload_to='portfolio/img/{author}/'),
        ),
    ]
