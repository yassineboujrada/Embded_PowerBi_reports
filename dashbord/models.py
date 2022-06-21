from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
YEAR_IN_SCHOOL_CHOICES = [
    ('minutes','Minutes'),
    ('day','Day'),
    ('week','Week'),
    ('month','Month'),
    ('year','Year'),
]

class Post(models.Model):

    title=models.CharField(max_length=250)
    format=models.CharField(
        max_length=10,
        choices=[
            ('img','IMAGE'),
            ('pdf','PDF FILE')
        ],
        default='pdf')
    delivery=models.TextField()
    every=models.IntegerField(default=2)
    reccurence=models.CharField(
        max_length=16,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='minutes',
    )
    date_posted=models.DateTimeField(default=timezone.now)
    author_user=models.ForeignKey(User,on_delete=models.CASCADE)# if author was deleting post also will be delet

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-create", kwargs={"pk": self.pk})
    
class microsoft_account(models.Model):

    client_id=models.TextField(null=False),
    client_secret=models.TextField(null=False),
    teneant_id=models.TextField(null=False),
    microsoft_user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.client_id