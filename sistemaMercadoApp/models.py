from django.db import models



class Produto(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=5, null=False, blank=False)
    validity = models.DateField(null=False, blank=False)
    bar_code = models.CharField(max_length=20, null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)

    objetos = models.Manager()




class Cliente(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)


class Endereco(models.Model):
    street_name = models.CharField(max_length=255, null=False, blank=False)
    neighborhood_name = models.CharField(max_length=255, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    client_id = models.ForeignKey(Cliente, related_name="enderecos", on_delete=models.DO_NOTHING)

class Pedido(models.Model):
    products_quant = models.PositiveIntegerField(null=False, blank=False)
    client_id = models.ForeignKey(Cliente, related_name="pedidos", null=False, blank=False, on_delete=models.DO_NOTHING)

class ProdutoPedido(models.Model):
    produto_id = models.ForeignKey (Produto, related_name="produtos_pedidos", on_delete=models.DO_NOTHING, null=False, blank=False)
    pedido_id = models.ForeignKey(Pedido, related_name="pedidos_produtos", on_delete=models.DO_NOTHING, null=False, blank=False)


