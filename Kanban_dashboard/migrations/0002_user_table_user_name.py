# Generated by Django 3.2.14 on 2022-07-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_table',
            name='user_name',
            field=models.CharField(default='Vinayak', max_length=100),
        ),
    ]
