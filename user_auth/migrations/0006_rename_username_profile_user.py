# Generated by Django 4.1.2 on 2023-01-05 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_rename_user_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
