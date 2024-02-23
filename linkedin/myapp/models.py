from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
    def get_full_name(self):
        return self.full_name
