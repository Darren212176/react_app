# Generated by Django 3.2.5 on 2021-07-18 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_list', '0002_rename_user_employee_created_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]