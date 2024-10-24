from django.db import models

class Abrigo(models.Model):
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")

    class Meta:
        verbose_name = 'Abrigo'
        verbose_name_plural = 'Abrigos'

    def __str__(self):
        return self.cnpj
