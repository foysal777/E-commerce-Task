from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class MyProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='myprofile')
    is_paid = models.BooleanField(default=False)
    stripe_session_id = models.CharField(max_length=200, blank= True, null= True)
   
    
def __str__(self):
        return self.user