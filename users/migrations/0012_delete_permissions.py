# Generated by Django 4.1.2 on 2022-11-03 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_permissions_alter_user_table_alter_userprofile_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Permissions',
        ),
    ]
