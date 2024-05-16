from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_citizen = models.BooleanField(default = False)
    age = models.PositiveIntegerField(default=0)


class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)