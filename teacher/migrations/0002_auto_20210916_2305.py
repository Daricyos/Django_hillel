# Generated by Django 3.2.5 on 2021-09-16 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.CharField(db_column='Subject', default=django.utils.timezone.now, max_length=200, verbose_name='Subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(db_column='Age', default=18, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(db_column='First name', max_length=200, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(db_column='Last name', max_length=200, verbose_name='Last name'),
        ),
    ]
