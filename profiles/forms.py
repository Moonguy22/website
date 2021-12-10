from django.contrib.auth.forms import UserCreationForm

from .models import MyUserModel

class SignupForm(UserCreationForm):
    class Meta:
        model = MyUserModel
        fields = ('username', 'password1', 'password2')
        