from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    # add additional fields in here
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
