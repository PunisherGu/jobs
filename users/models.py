from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)
