from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    
    def __str__(self):
        return str(self.username)

class Message(models.Model):
    recipient = models.name = models.ForeignKey(User, related_name = 'recipient', on_delete = models.CASCADE)
    content = models.CharField(max_length = 1000)
    
    def __str__(self):
        return str(self.content)

