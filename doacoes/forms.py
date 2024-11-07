from django import forms
from .models import Doacao

class DoacaoModelForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'

        error_messages = {

            'data_doacao': {
                'required': 'A data da doação é um campo obrigatório'
            },
            'valor': {
                'required': 'O valor da doação é um campo obrigatório',
                'invalid': 'Por favor, insira um valor válido'
            },
            'tipo_doacao': {
                'required': 'O tipo de doação é um campo obrigatório'
            },
            'status': {
                'required': 'O status da doação é um campo obrigatório'
            },
        }
