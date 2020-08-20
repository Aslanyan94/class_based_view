from django.contrib.auth.models import User
from django.db import models


# class User(models.Model):
#     first_name = models.CharField(max_length=30)


class People(models.Model):
    # user = models.ForeignKey(User)
    # timestamp = models.DatetimeField()
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname


# class Worker(models.Model):
#     people = models.ForeignKey(User)