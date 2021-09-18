# Generated by Django 3.2.5 on 2021-09-16 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_alter_groups_group_name'),
        ('students', '0006_alter_student_in_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='in_group',
            field=models.ForeignKey(db_column='Group ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='group.groups', verbose_name='Group ID'),
        ),
    ]
