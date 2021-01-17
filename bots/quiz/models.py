from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Round(models.Model):
    rounds=models.IntegerField(default=1, null=False)
    question=models.CharField(max_length=500, null=False)
    answer=models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.rounds)

class Profile(models.Model):
    name=models.CharField(max_length=100, null=False)
    email=models.EmailField(max_length=100, null=False)
    score=models.IntegerField(default=0)
    curr_round=models.IntegerField(default=1)
    submit_time=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
	
