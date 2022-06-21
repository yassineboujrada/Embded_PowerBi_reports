# Generated by Django 4.0.4 on 2022-06-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0004_alter_post_reccurence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='format',
            field=models.CharField(choices=[('img', 'IMAGE'), ('pdf', 'PDF FILE')], default='pdf', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='reccurence',
            field=models.CharField(choices=[('minutes', 'Minutes'), ('day', 'Day'), ('week', 'Week'), ('year', 'Year')], default='minutes', max_length=16),
        ),
    ]
