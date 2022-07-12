# Generated by Django 4.0.4 on 2022-06-29 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashbord', '0015_alter_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='web_url',
            new_name='delivery',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='format',
            field=models.CharField(choices=[('pdf', 'PDF File'), ('img', 'IMAGE'), ('ppt', 'Power Point'), ('pptx', 'Power Point'), ('pdf', 'PDF FILE')], default='pdf', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='reccurence',
            field=models.CharField(choices=[('minutes', 'Minutes'), ('hour', 'Hour'), ('day', 'Day'), ('week', 'Week'), ('month', 'Month'), ('year', 'Year')], default='minutes', max_length=19),
        ),
    ]
