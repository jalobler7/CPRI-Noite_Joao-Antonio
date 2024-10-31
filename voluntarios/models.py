from django.db import models
import abrigo.models

class Voluntario(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome do voluntário')
    idade = models.IntegerField('Idade', help_text='Idade do voluntário')
    cpf = models.CharField('CPF', max_length=11, help_text='CPF do voluntário', unique=True)
    email = models.EmailField('Email', help_text='Email do voluntário')
    endereco = models.CharField('Endereço', max_length=200, help_text='Endereço do voluntário')
    quantidade = models.IntegerField('Quantidade', help_text='Quantidade associada ao voluntário')

    abrigo = models.ForeignKey(abrigo.models.Abrigo, verbose_name=' Abrigo', help_text='Nome do abrigo',
                               on_delete=models.CASCADE, related_name='abrigo')

    class Meta:
        verbose_name = 'Voluntário'
        verbose_name_plural = 'Voluntários'

    def __str__(self):
        return self.nome