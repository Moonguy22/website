from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from app.models import Product


class MyUserManager(BaseUserManager):

    def create_user(self, username, password):
        user = self.model(
            username=self.normalize_email(username),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})   


class MyUserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=36, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = MyUserManager()
    
    def save(self, *args, **kwargs):
        super(MyUserModel, self).save(*args, **kwargs)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    text = models.CharField(max_length=200)
    title = models.CharField(max_length=20)
    user = models.ForeignKey(MyUserModel, related_name='comments', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
        