# Generated by Django 5.0 on 2023-12-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_add_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_task',
            name='date',
            field=models.DateField(),
        ),
    ]
