from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUser(User):
    
    score = models.IntegerField(_("score points"), default=0)
    
    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"