# Generated by Django 4.0.4 on 2022-06-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0002_microsoft_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='format',
            field=models.CharField(choices=[('img', 'IMAGE'), ('pdf', 'PDF FILE')], default='img', max_length=10),
        ),
    ]
