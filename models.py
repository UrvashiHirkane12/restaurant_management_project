from django.db import models

class Feedback(models.Model):
    comment= models.TextField()
    created_at = models.dateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} - {self.created_at.strftime('%y-%m-%d')}"