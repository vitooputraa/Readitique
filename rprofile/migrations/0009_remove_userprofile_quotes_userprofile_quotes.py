# Generated by Django 4.2.4 on 2023-10-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rprofile', '0008_remove_userprofile_text_userprofile_quotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='quotes',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='quotes',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
