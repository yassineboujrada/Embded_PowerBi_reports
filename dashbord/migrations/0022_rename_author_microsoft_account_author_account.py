# Generated by Django 4.0.4 on 2022-07-05 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0021_alter_microsoft_account_email_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='microsoft_account',
            old_name='author',
            new_name='author_account',
        ),
    ]