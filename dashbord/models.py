# from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class Post(models.Model):
    title=models.CharField(max_length=2500)
    delivery=models.TextField(null=True)
    format=models.CharField(
        max_length=30,
        choices=[
            ('pdf','PDF File'),
            # ('img','IMAGE'),
            ('ppt','Power Point'),
            # ('pptx','Power Point'),
            # ('pdf','PDF FILE')
        ],
        default='pdf')
    at=models.TimeField(auto_now=False,default=datetime.datetime.now(),null=True)
    every=models.IntegerField(default=2)
    reccurence=models.CharField(
        max_length=19,
        choices=[
            ('minutes','Minutes'),
            ('hour','Hour'),
            ('day','Day'),
            ('week','Week'),
            ('month','Month'),
            ('year','Year'),
        ],
        default='minutes',
    )
    url_of_reports=models.TextField(null=True)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE, default='')# if author was deleting post also will be delet

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("userinfos", kwargs={"pk": self.pk})
    
class microsoft_account(models.Model):
    email_account=models.CharField(max_length=700)
    password_accoount=models.TextField(null=False,default='')
    client_id=models.TextField(null=False,default='')
    client_secret=models.TextField(null=False,default='')
    teneant_id=models.TextField(null=False,default='')
    path_of_json=models.TextField(null=False,default='')
    author_account=models.ForeignKey(User,on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.email_account

    def get_absolute_url(self):
        return reverse("userinfos", kwargs={"pk": self.pk})