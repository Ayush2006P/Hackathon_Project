from django.db import models

# Create your models here.

class register(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.email

