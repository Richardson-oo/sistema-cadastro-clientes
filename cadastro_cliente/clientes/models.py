from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True) # unique = true => garante que os valores inseridos nesse campo seja unicos
    telefone = models.CharField(max_length=15, blank=True, null=True) # blank campos não são obrigatorios
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

