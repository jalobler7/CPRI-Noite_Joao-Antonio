from django.db import models

class Abrigo(models.Model):
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")

    def __str__(self):
        return f"Abrigo {self.cnpj} - {self.endereco}"
