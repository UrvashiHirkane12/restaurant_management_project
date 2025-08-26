from django.db import models
from django contrib.auth.models import user

class Feedback(models.Model):
    comment= models.TextField()
    created_at = models.dateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} - {self.created_at.strftime('%y-%m-%d')}"


class userprofile(models.model):
    user = models.onetoonefieldO(user, name="profile")        
    name = models.charfield(max_length=100)
    email= models.emailfield(unique=True)


def __str__(self):
    return self.user.username