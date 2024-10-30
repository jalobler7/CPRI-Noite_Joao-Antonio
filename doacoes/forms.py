from django import forms
from .models import Doacao

class DoacaoModelForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'

        error_messages = {
            'quantidade': {
                'required': 'A quantidade da doação é um campo obrigatório'
            },
            'unidade': {
                'required': 'A unidade de medida é um campo obrigatório'
            },
            'tipo': {
                'required': 'O tipo de doação é um campo obrigatório'
            },
        }
