from django import forms

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
            'quantidade': {'required': 'A quantidade é um campo obrigatório'},
        }
