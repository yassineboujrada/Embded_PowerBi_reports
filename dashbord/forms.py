from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.utils import timezone

class Create_new_playlist(forms.Form):

    title = forms.CharField(max_length=250 , widget=forms.TextInput({'placeholder':'title mn backend'}))
    format=forms.ChoiceField(choices=(('img','IMAGE'),('pdf','PDF FILE')))
    delivery = forms.CharField(max_length=250,widget=forms.TextInput({'placeholder':'separete between emails by " , "'}))
    reccurence=forms.ChoiceField(choices=(('min','Minutes'),
            ('d','Day'),
            ('week','Week'),
            ('y','Year')))
    date_save = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(Create_new_playlist, self).__init__(*args, **kwargs)

        for fieldname in ["title", "format" ,"delivery" , "reccurence", "date_save"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model=Post
        fields='__all__'  
