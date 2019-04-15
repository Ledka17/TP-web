from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.USERNAME_FIELD

#class Question_Manager(model.Model):


class Question(models.Model):
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=128)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
