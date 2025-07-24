from django.contrib.auth.models import AbstractUser
from django.db import models

from .mixins import SlugMixin
from .managers import UserManager
from .enums import Role


class User(AbstractUser, SlugMixin):
    email = models.EmailField(unique=True, max_length=125, null=True)
    avatar = models.ImageField(upload_to='avatars/%y/%m/%d', null=True, blank=True)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT
    )
    
    objects = UserManager()
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.get_full_name() or self.username
    
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    