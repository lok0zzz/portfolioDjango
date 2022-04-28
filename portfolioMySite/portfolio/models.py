from django.db import models


class Linguagem(models.Model):
    linguagem_nome = models.CharField(max_length=50)

    def __str__(self):
        return self.linguagem_nome

    class Meta:
        ordering = ['linguagem_nome']


class Projeto(models.Model):
    nome_do_projeto = models.CharField(max_length=40)
    descricao = models.TextField(null=True, blank=True)
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE)
    repositorio = models.CharField(max_length=60, default='Sem repositório.')
    imagem = models.CharField(blank=True, null=True, max_length=4000)

    def __str__(self):
        return self.nome_do_projeto

    class Meta:
        ordering = ['-id']