from django.db import models
from django.contrib.auth.models import User

class todo(models.Model):
    text = models.CharField(max_length= 40)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.text