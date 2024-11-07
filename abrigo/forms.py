from django import forms
from django.forms import inlineformset_factory


from .models import Abrigo

class AbrigoModelForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O endereco é um campo obrigatório'},
            'cnpj' : {'required': 'O CNPJ do Abrigo é um campo obrigatório', 'unique': 'CNPJ já cadastrado'},
            'endereco' : {'required': 'O endereco é um campo obrigatório'},
        }

