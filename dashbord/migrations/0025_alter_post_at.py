# Generated by Django 4.0.4 on 2022-07-19 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0024_alter_post_at_alter_post_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='at',
            field=models.TimeField(default=datetime.datetime(2022, 7, 19, 12, 28, 23, 541017), null=True),
        ),
    ]
