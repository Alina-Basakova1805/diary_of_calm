from django.db import models
from django.contrib.auth.models import User

class DiEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="entries")
    title = models.CharField(max_length= 100)
    memo = models.TextField()
    creted_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title