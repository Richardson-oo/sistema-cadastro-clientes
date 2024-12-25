from django.urls import path
from . import views

urlpatterns =[
    path('', views.lista_cliente, name= 'lista_cliente' ),
    path('add/', views.adicionar_cliente, name= 'adicionar_cliente'),
    path('detalhes/<int:cliente_id>/', views.detalhes, name= 'detalhes'),
    path('editar_cliente/<int:cliente_id>/', views.edit_cliente, name= 'edit_cliente'),
    path('clientes/delete/<int:cliente_id>/', views.delete_cliente, name='delete_cliente'),
]
