# Generated by Django 4.0.4 on 2022-06-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0008_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url_of_reports',
            field=models.TextField(null=True),
        ),
    ]
