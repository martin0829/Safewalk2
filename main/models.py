from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .validators import validate_email

class Region(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

class Party(models.Model):
    startLoc = models.ManyToManyField(Region, related_name='start')
    endLoc = models.ManyToManyField(Region, related_name='end')
    departTime = models.TimeField()

class Walker(AbstractBaseUser):
    username = models.CharField(max_length=200)
    USERNAME_FIELD = 'username'
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True, validators=[validate_email])
    photo = models.ImageField(upload_to="walkers/profile/")
    rating = models.IntegerField()
    emgContact = models.CharField(max_length=200)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, blank=True, null=True)

