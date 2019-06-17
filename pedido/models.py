from django.db import models
from pecas.models import Pecas
from enderecoEntrega.models import EnderecoEntrega
from cliente.models import Cliente

class Pedido(models.Model):


    descricaoPeca = models.ForeignKey(Pecas, on_delete=models.CASCADE)
    enderecoEntrega = models.ForeignKey(EnderecoEntrega, on_delete=models.CASCADE)
    infoContato = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    statusDeFinalizacao = models.CharField(max_length=7)


    def __str__(self):
        return self.statusDeFinalizacao
