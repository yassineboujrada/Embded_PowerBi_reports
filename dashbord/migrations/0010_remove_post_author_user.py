# Generated by Django 4.0.4 on 2022-06-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0009_post_url_of_reports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_user',
        ),
    ]
