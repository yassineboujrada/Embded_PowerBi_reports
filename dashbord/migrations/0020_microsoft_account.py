# Generated by Django 4.0.4 on 2022-07-05 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashbord', '0019_delete_microsoft_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='microsoft_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_account', models.CharField(default='admin', max_length=700)),
                ('password_accoount', models.TextField(default='')),
                ('client_id', models.TextField(default='')),
                ('client_secret', models.TextField(default='')),
                ('teneant_id', models.TextField(default='')),
                ('path_of_json', models.TextField(default='')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
