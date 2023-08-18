from django.db import models

# Create your models here.
#Usermodel
class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(null=True, unique=True)
    bio = models.TextField(null=True)


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Ballots(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', 'created']
    
    def __str__(self):
        return self.name 


class Comment(models.Model):
    REACTIONS = [
            ("L" , "Like"),
            ("U" , "unlike"),
            ("N" , "neutral")
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ballot = models.ForeignKey(Ballots, on_delete = models.CASCADE)
    body = models.TextField()
    # reaction = models.CharField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[0:50]


