from django.db import models

class Pecas(models.Model):
    nome =  models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.descricao