# Generated by Django 4.1.2 on 2022-10-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0014_alter_comment_options_alter_comment_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_added',
            field=models.TimeField(auto_now_add=True, db_index=True),
        ),
    ]
