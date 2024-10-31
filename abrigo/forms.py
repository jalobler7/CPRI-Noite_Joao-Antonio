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


#ProdutosServicoInLine = inlineformset_factory(Servico, ProdutosServico, fk_name= 'servico',
 #fields=('produto','quantidade'),extra=1, can_delete=True)

# VoluntarioAbrigoInLine = inlineformset_factory(
#     Abrigo,
#     VoluntariosAbrigo,
#     fk_name='abrigo',  # Definindo a chave estrangeira para Abrigo
#     fields=('voluntario', 'quantidade'),  # Campos a serem exibidos no formset
#     extra=1,
#     can_delete=True
# )