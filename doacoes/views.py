from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from .forms import DoacaoModelForm
from .models import Doacao

class DoacoesView(ListView):
    model = Doacao
    template_name = 'doacoes.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(DoacoesView, self).get_queryset()

        if buscar:
            return qs.filter(tipo__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)  # Ajuste o número de itens por página conforme necessário
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            messages.info(self.request, 'Não existem doações cadastradas')
            return qs


class DoacaoAddView(SuccessMessageMixin, CreateView):
    model = Doacao
    form_class = DoacaoModelForm
    template_name = 'doacao_form.html'
    success_url = reverse_lazy('doacoes')
    success_message = 'Doação cadastrada com sucesso'


class DoacaoUpdateView(SuccessMessageMixin, UpdateView):
    model = Doacao
    form_class = DoacaoModelForm
    template_name = 'doacao_form.html'
    success_url = reverse_lazy('doacoes')
    success_message = 'Doação atualizada com sucesso'


class DoacaoDeleteView(SuccessMessageMixin, DeleteView):
    model = Doacao
    template_name = 'doacoes_apagar.html'
    success_url = reverse_lazy('doacoes')
    success_message = 'Doação deletada com sucesso'
