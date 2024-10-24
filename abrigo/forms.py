from django import forms

from .models import Abrigo

class AbrigoModelForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = '__all__'

        error_messages = {
            'cnpj' : {'required': 'O CNPJ do Abrigo é um campo obrigatório', 'unique': 'CNPJ já cadastrado'},
            'endereco' : {'required': 'O endereco é um campo obrigatório'},
        }