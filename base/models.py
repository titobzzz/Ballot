from django.db import models

# Create your models here.
#Usermodel
class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(null=True, unique=True)
    bio = models.TextField(null=True)

    # avatar