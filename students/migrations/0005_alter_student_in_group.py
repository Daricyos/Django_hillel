# Generated by Django 3.2.5 on 2021-09-16 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_rename_group_students_groups_group_student'),
        ('students', '0004_auto_20210916_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='in_group',
            field=models.ForeignKey(db_column='Group ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='group.groups', verbose_name='Group ID'),
        ),
    ]
