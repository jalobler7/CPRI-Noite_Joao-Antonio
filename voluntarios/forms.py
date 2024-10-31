from django import forms
from django.forms import inlineformset_factory

from .models import Voluntario

class VoluntarioModelForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do Voluntário é um campo obrigatório'},
            'idade': {'required': 'A idade é um campo obrigatório'},
            'cpf': {'required': 'O CPF do Voluntário é um campo obrigatório', 'unique': 'CPF já cadastrado'},
            'email': {'required': 'O email é um campo obrigatório'},
            'endereco': {'required': 'O endereço é um campo obrigatório'},

        }


    # VoluntariosAbrigoInLine = inlineformset_factory(
    #     Voluntario,  #
    #     VoluntariosAbrigo,  #
    #     fk_name='voluntario',
    #     fields=('abrigo'),
    #     extra=1,
    #     can_delete=True
    # )