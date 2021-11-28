from django.db import models

class Quiz(models.Model):
    category = models.CharField(
      max_length=100,unique=True
    )
    
    @property
    def is_available(self):
      if not hasattr(self,'questions'):
          return False
      return self.questions.all().count() == 10
      
    def __str__(self):
        return self.category
