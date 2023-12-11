from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class feature(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=150)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # test=models.

    def __str__(self):
        return self.name


class message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(feature, on_delete=models.SET_NULL, null=True)

    body = models.TextField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
