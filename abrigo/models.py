from django.db import models
#
# from voluntariosabrigo.models import VoluntariosAbrigo


class Abrigo(models.Model):

    nome = models.CharField(max_length=255, verbose_name="Nome", default='Exemplo de nome')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")


    # voluntarios = models.ManyToManyField(to = 'voluntarios.Voluntarios', through= 'voluntariosabrio.VoluntariosAbrigo')
    #
    # def voluntarios(self):
    #     return VoluntariosAbrigo.objects.filter(abrigo=self)


    class Meta:
        verbose_name = 'Abrigo'
        verbose_name_plural = 'Abrigos'

    def __str__(self):
        return self.nome
