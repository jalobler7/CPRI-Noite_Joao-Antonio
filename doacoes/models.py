from django.db import models

class Doacao(models.Model):
    quantidade = models.FloatField('Quantidade', help_text='Quantidade da doação')
    unidade = models.IntegerField('Unidade', help_text='Unidade de medida associada à doação')
    tipo = models.CharField('Tipo', max_length=100, help_text='Tipo de item doado')

    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

    def __str__(self):
        return f"{self.tipo} - {self.quantidade} ({self.unidade})"