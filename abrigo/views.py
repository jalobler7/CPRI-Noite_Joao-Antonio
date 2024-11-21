from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Count

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Abrigo

from .forms import AbrigoModelForm


class AbrigoExibir(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Abrigo
    template_name = 'abrigo_exibir.html'

    permission_required =  'abrigo.view_abrigo'
    permission_denied_message = 'Listar Abrigos'

    def get_object(self, queryset=None):

        return get_object_or_404(Abrigo, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['doacoes'] = self.object.doacoes_relacionadas.all()
        return context


class AbrigosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Abrigo
    template_name = 'abrigos.html'
    context_object_name = 'abrigos'
    paginate_by = 5
    permission_required = 'abrigo.view_abrigo'
    permission_denied_message = 'Listar Abrigos'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')


        qs = Abrigo.objects.annotate(qtd_voluntarios=Count('voluntario'))


        if buscar:
            qs = qs.filter(endereco__icontains=buscar)

        return qs


class AbrigoAddView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'abrigo.add_abrigo'
    permission_denied_message = 'Adcionar Abrigos'
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo cadastrado com sucesso'



class AbrigoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo atualizado com sucesso'
    permission_required = 'abrigo.change_abrigo' #change
    permission_denied_message = 'Editar Abrigos'


class AbrigoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Abrigo
    template_name = 'abrigo_apagar.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo deletado com sucesso'
    permission_required = 'abrigo.delete_abrigo'
    permission_denied_message = 'Deletar Abrigos'



