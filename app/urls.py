from django.urls import path
from .views import main, detail



app_name = 'app'
urlpatterns = [
    path('', main, name='main'),
    path('detail/<int:pk>/',detail, name='detail')
]