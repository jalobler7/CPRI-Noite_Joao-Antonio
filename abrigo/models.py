from django.db import models
from django.db.models import CASCADE


class Abrigo(models.Model):

    nome = models.CharField(max_length=255, verbose_name="Nome", default='Exemplo de nome')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")

    voluntarios = models.ForeignKey('voluntarios.Voluntario', verbose_name='Voluntario', related_name="tste",
                                     on_delete=models.CASCADE, null=True,blank=True)



    class Meta:
        verbose_name = 'Abrigo'
        verbose_name_plural = 'Abrigos'
        permissions = (('Visualizar_Doacoes', 'Permite visualizar as doacoes'),)

    def __str__(self):
        return self.nome
