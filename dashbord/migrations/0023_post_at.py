# Generated by Django 4.0.4 on 2022-07-08 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0022_rename_author_microsoft_account_author_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='at',
            field=models.TimeField(default=datetime.datetime(2022, 7, 8, 19, 9, 23, 50694)),
        ),
    ]
