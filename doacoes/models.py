from django.db import models
import abrigo.models

class Doacao(models.Model):
    TIPO_DOACAO_CHOICES = [
        ('MONETARIA', 'Monetária'),
        ('MATERIAL', 'Material'),
        ('SERVICO', 'Serviço'),
    ]

    STATUS_DOACAO_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDA', 'Concluída'),
        ('PROCESSANDO', 'Processando'),
    ]


    data_doacao = models.CharField('Data da Doação',max_length=20, help_text='Data em que a doação foi realizada')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, help_text='Valor da doação')
    tipo_doacao = models.CharField('Tipo de Doação', max_length=20, choices=TIPO_DOACAO_CHOICES, help_text='Tipo de doação')
    status = models.CharField('Status', max_length=20, choices=STATUS_DOACAO_CHOICES, help_text='Status da doação')


    abrigo = models.ForeignKey('abrigo.Abrigo', verbose_name=' Abrigo', help_text='Nome do abrigo',
                               on_delete=models.CASCADE, related_name='doacoes_relacionadas')

    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

    def __str__(self):
        return f"{self.tipo_doacao}"
