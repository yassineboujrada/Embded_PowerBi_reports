from calendar import c
from attr import fields
from django import forms
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateform(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User 
        fields=['username'] 
    
    # def __init__(self, *args, **kwargs):
    #     super(UserUpdateform, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class': 'text-primary'})

# class Create_new_playlist(forms.Form):

#     title = forms.CharField(max_length=250 , widget=forms.TextInput({'placeholder':'title mn backend'}))
#     format=forms.ChoiceField(choices=(('img','IMAGE'),('pdf','PDF FILE')))
#     delivery = forms.CharField(max_length=250,widget=forms.TextInput({'placeholder':'separete between emails by " , "'}))
#     reccurence=forms.ChoiceField(choices=(('min','Minutes'),
#             ('d','Day'),
#             ('week','Week'),
#             ('y','Year')))
#     date_save = forms.CharField()

#     def __init__(self, *args, **kwargs):
#         super(Create_new_playlist, self).__init__(*args, **kwargs)

#         for fieldname in ["title", "format" ,"delivery" , "reccurence", "date_save"]:
#             self.fields[fieldname].help_text = None

#     class Meta:
#         model=Post
#         fields='__all__'  

# class post_playlist(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields=['title','delivery','format','every','reccurence']
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # self.fields['author_user'].queryset = User.objects.filter(pk=pk)
#         # self.fields['url_of_reports'].queryset = " ".join(url)