from django.contrib import admin

from profiles.forms import CommentForm
from .models import MyUserModel, Comment

admin.site.register(MyUserModel)
admin.site.register(Comment)