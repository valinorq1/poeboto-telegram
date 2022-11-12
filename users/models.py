from django.db import models
from django.contrib.auth.models import AbstractUser
from service import models as service_models

from . import managers

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    email = models.EmailField('почта', unique=True)
    balance = models.IntegerField('баланс', default=0)

    objects = managers.UserManager()
