from django.shortcuts import render
from django.views.generic  import ListView

from sistemaMercadoApp.models import Cliente, Produto


# Create your views here.

class ListClientes(ListView):
    template_name = "clientes.html"
    model = Cliente
    context_object_name = "clientes"

class ListProdutos(ListView):
    template_name = "produtos.html"
    model = Produto
    context_object_name = "produtos"



# def listar_clientes(request):
#     clientes = Cliente.objects.all()
#
#     contexto = {'clientes': clientes}
#
#     return render(request, )
