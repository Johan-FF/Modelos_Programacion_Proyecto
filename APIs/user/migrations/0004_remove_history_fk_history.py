# Generated by Django 4.1.7 on 2023-03-14 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_fk_country_alter_user_fk_history_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='fk_history',
        ),
    ]
