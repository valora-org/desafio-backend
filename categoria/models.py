from django.db import models


class Categoria(models.Model):
    nome = models.TextField(max_length=100)

    def __str__(self):
        return self.nome
