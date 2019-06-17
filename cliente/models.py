from django.db import models

class Cliente(models.Model):

    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=12)
    email = models.CharField(max_length=12)

    def __str__(self):
        return self.telefone