from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.forms import FloatField
from django.urls import reverse
from django.db.models import Avg, Sum


class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not phone:
            raise ValueError('Users must have an phone')
        # user = self.model(email=self.normalize_email(email), **extra_fields)
        user = self.model(
            phone=phone,
            name=extra_fields.get('name'),
            line_id=extra_fields.get('line_id'),
            apple_id=extra_fields.get('apple_id'),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password, **extra_fields):
        """Creates and saves a new super user"""
        user = self.create_user(phone, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=10, unique=True)
    objects = UserManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    name = models.CharField(max_length=255, null=True)

    email = models.CharField(max_length=100, blank=True, null=True)

    line_id = models.CharField(
        max_length=100, blank=True, null=True, unique=True)
    apple_id = models.CharField(
        max_length=100, blank=True, null=True, unique=True)

    USERNAME_FIELD = 'phone'


class Drawdata(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    jsondata = models.TextField(null=True)

    def __str__(self):
        return self.name
