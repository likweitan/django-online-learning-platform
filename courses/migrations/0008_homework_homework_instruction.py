# Generated by Django 3.2 on 2021-04-18 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_rename_homework_due_date_homework_homework_due_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='homework_instruction',
            field=models.TextField(default=10000),
            preserve_default=False,
        ),
    ]