from django.db import models

# Create your models here.
from django.contrib import auth

# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)



