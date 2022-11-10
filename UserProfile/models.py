from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    about_yourself = models.TextField(max_length=5000, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.title