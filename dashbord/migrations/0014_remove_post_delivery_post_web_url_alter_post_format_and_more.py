# Generated by Django 4.0.4 on 2022-06-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0013_alter_post_format'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='delivery',
        ),
        migrations.AddField(
            model_name='post',
            name='web_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='format',
            field=models.CharField(choices=[('pdf', 'PDF File'), ('img', 'IMAGE'), ('ppt', 'Power Point'), ('pptx', 'Power Point'), ('pdf', 'PDF FILE')], default='pdf', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
