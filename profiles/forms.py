from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MyUserModel, Comment
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')
    

class SignupForm(UserCreationForm):
    class Meta:
        model = MyUserModel
        fields = ('username', 'password1', 'password2')
        
class FeedBackForm(forms.Form):
    number = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    text = forms.CharField(max_length=200)