from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=127, verbose_name='имя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
