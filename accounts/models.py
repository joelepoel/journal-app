from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): #to extend the base User model
    email = models.EmailField(unique=True) #Email has to be unique
