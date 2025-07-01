from django.db import models
from django.contrib.auth.models import User

class DiEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="entries",null=True)
    image = models.ImageField(upload_to ='entry_images/',null=True,blank=True)
    title = models.CharField(max_length= 100,null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
def __str__(self):
   return f"{self.user.username} - {self.created_at} - {self.image}"