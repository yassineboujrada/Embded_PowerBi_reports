# Generated by Django 4.0.5 on 2022-06-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0005_alter_post_format_alter_post_reccurence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reccurence',
            field=models.CharField(choices=[('minutes', 'Minutes'), ('day', 'Day'), ('week', 'Week'), ('month', 'Month'), ('year', 'Year')], default='minutes', max_length=16),
        ),
    ]