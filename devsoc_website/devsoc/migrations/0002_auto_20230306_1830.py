# Generated by Django 2.2 on 2023-03-06 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devsoc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='noticeimage',
            name='topic',
        ),
    ]
