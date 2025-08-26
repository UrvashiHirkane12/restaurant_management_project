from django.db import models
from django contrib.auth.models import user
from django contrib.auth.models import abstractuser

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


class customeruser(abstractuser):
    name= models.charfield(max_length=100)
    email=  models.emailfield(unique=True)
    def __str__(self):
        return self.username

class menu(models.Model):
    name = models.CharField(max_lentg=100)
    price=  models.DecimalField(max_digits=8)

    def__str__(self):
        return self.name

class order(models.Model):
    STATUS_CHOICES =[
        ("PENDING", "pending"),
        ("CONFIRMED","confirmed"),
        ("DELIVERED" , "delivered"),
    ] 

    def __str__(self):
        return f"Order  #{self.id} by {self.customer.username}"       


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.emailField()
    submitted_at = models.dateTimeField(auto_now_add=True)

    def__str__(self):
        return self.name