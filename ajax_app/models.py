from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



# Create your models here.
