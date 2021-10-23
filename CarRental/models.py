from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    SSN = models.IntegerField(unique=True)
    Car_License_Number = models.CharField(max_length=8, null=True, blank=True)
    Picture_For_Car_License_Number = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}\n{self.email}"
