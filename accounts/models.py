
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # you can add extra fields later if needed
    # example:
    # bio = models.TextField(blank=True)
    pass

    def __str__(self):
        return self.username
