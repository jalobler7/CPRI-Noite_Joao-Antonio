from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from .forms import DoacaoModelForm
from .models import Doacao

class DoacoesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Doacao
    template_name = 'doacoes.html'
    # permission_required = 'abrigos.delete_abrigo'
    # permission_denied_message = 'Deletar Abrigos'
    permission_required = 'doacoes.view_doacao'
    permission_denied_message = 'Listar Doacoes'

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


class DoacaoAddView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Doacao
    form_class = DoacaoModelForm
    permission_required = 'doacoes.view_doacao'
    permission_denied_message = 'Listar Doacoes'
    template_name = 'doacao_form.html'
    success_url = reverse_lazy('doacoes')
    success_message = 'Doação cadastrada com sucesso'


class DoacaoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Doacao
    form_class = DoacaoModelForm
    template_name = 'doacao_form.html'
    success_url = reverse_lazy('doacoes')
    success_message = 'Doação atualizada com sucesso'
    permission_required = 'doacoes.change_doacao'
    permission_denied_message = 'Editar Doacoes'


class DoacaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Doacao
    template_name = 'doacoes_apagar.html'
    success_url = reverse_lazy('doacoes')
    success_message = 'Doação deletada com sucesso'
    permission_required = 'doacoes.delete_doacao'
    permission_denied_message = 'Deletar Doacoes'
