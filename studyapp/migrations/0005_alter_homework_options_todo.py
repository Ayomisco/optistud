# Generated by Django 4.1.2 on 2022-12-17 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studyapp', '0004_homework'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['-created_at'], 'verbose_name': 'Homework', 'verbose_name_plural': 'Homework'},
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ToDo',
                'verbose_name_plural': 'ToDos',
                'ordering': ['-created_at'],
            },
        ),
    ]