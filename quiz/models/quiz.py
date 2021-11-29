from django.db import models

class Quiz(models.Model):
    category = models.CharField(
      max_length=100,unique=True
    )
    
    def __str__(self):
        return self.category
