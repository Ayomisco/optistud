# Generated by Django 4.1.2 on 2022-11-11 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_rename_url_profile_github_url_profile_facebook_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone NO.'),
        ),
    ]
