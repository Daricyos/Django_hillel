# Generated by Django 3.2.5 on 2021-09-16 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_logger'),
        ('teacher', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='group_student',
        ),
        migrations.AddField(
            model_name='groups',
            name='group_curator',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
        migrations.AddField(
            model_name='groups',
            name='group_headman',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AddField(
            model_name='groups',
            name='group_students',
            field=models.IntegerField(null=True),
        ),
    ]
