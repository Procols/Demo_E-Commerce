from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    Name = models.OneToOneField(User, on_delete=models.CASCADE) 
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=200)  

    def __str__(self):
        return self.Name.username

