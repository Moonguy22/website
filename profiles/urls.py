from django.urls import path
from .views import signup, add_comment, feedback
from django.urls import path

app_name = 'profiles'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('comment/<int:pk>', add_comment, name='add_comment'),
    path('feedback', feedback, name='feedbaack')
]