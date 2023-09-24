import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, upload_to='images/')
    usdc = models.CharField(null=True, default=0, max_length=200)
    btc = models.CharField(null=True, default=0, max_length=200)
    eth = models.CharField(null=True, default=0, max_length=200)
    usd = models.CharField(null=True, default=0, max_length=200)
    cny = models.CharField(null=True, default=0, max_length=200)
    hkd = models.CharField(null=True, default=0, max_length=200)
    jpy = models.CharField(null=True, default=0, max_length=200)
    gbp = models.CharField(null=True, default=0, max_length=200)
    eur = models.CharField(null=True, default=0, max_length=200)
    usdt = models.CharField(null=True, default=0, max_length=200)

    def __str__(self):
        return str(self.user)