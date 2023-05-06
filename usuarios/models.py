from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser): # sobrescreve a classe AbstractUser p/ acrescentar um novo campo "cargo".
    choices_cargo = (('V', 'Vendedor'),
                     ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)