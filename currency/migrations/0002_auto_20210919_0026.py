# Generated by Django 3.2.5 on 2021-09-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='source',
            field=models.CharField(max_length=20),
        ),
    ]
