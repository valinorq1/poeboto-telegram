
from typing import Dict, Union

from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
  user_in_migrations = True

  def _create_user(self, email: str, password: str, **extra_fields: Dict) -> models.Model:
    if not email:
      raise ValueError('Email must be set')

    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email: str, password: Union[str, None] = None, **extra_fields: Dict) -> models.Model:
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email: str, password: str, **extra_fields: Dict) -> models.Model:
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True')

    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True')

    return self._create_user(email, password, **extra_fields)
