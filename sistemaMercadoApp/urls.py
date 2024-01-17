from django.urls import path

from sistemaMercadoApp import views

urlpatterns = [
    path('get_all_clientes/', views.ListClientes.as_view(), name="ListClientes"),
    path('get_all_produtos/', views.ListProdutos.as_view(), name="ListProdutos")
]
