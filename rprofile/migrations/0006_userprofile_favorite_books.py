# Generated by Django 4.2.4 on 2023-10-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_book_user'),
        ('rprofile', '0005_alter_userprofile_email_alter_userprofile_handphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorite_books',
            field=models.ManyToManyField(blank=True, to='main.book'),
        ),
    ]
