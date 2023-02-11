from django.db import models


class Projetos(models.Model):
    nome = models.CharField(max_length=200,null=False,blank=False)
    imagem = models.ImageField(upload_to="ImagemProjetos/%Y/%m/%d/",blank=True)
    legenda = models.CharField(max_length=255,null=False,blank=False)
    descricao = models.TextField(null=False,blank=True)
    link_projeto = models.CharField(max_length=255,null=False,blank=True)

    def __str__(self):
        return f'{self.nome}'
