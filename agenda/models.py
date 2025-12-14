from django.db import models
from django.contrib.auth.models import User


class Contato(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)

    # Dados Escolares (Personalização do Diretor)
    turma = models.CharField(max_length=50, blank=True, null=True, verbose_name="Turma/Série")
    ano = models.PositiveIntegerField(blank=True, null=True, verbose_name="Ano Letivo")

    # Contato
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    # Endereço
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']