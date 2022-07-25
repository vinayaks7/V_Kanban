# Generated by Django 3.2.14 on 2022-07-23 16:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Table',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_desc', models.CharField(default='DESC', max_length=100)),
                ('task_status', models.CharField(default='STATUS', max_length=100)),
                ('task_priority', models.IntegerField(default='3')),
                ('task_summary', models.CharField(default='SUMMARY', max_length=50)),
                ('task_assignee', models.CharField(default='Self', max_length=50)),
                ('task_deadline', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User_Table',
            fields=[
                ('user_id', models.AutoField(default='user', primary_key=True, serialize=False)),
                ('password', models.CharField(default='pass', max_length=50)),
                ('task_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Kanban_dashboard.task_table')),
            ],
        ),
    ]
