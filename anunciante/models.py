from django.db import models

class Anunciante(models.Model):

    nome =  models.CharField(max_length=150)
    senha = models.CharField(max_length=8)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome