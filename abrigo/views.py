from lib2to3.fixes.fix_input import context

from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin

from doacoes.models import Doacao
from voluntarios.models import Voluntario
from .forms import AbrigoModelForm
from .models import Abrigo
#from .forms import ServicoModelForm, ProdutosServicoInLine
from .forms import AbrigoModelForm


class AbrigoExibir(DetailView):
    model = Abrigo
    template_name = 'abrigo_exibir.html'

    def get_object(self, queryset=None):

        return get_object_or_404(Abrigo, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['doacoes'] = self.object.doacoes_relacionadas.all()
        return context


class AbrigosView(ListView):
    model = Abrigo
    template_name = 'abrigos.html'
    context_object_name = 'abrigos'
    paginate_by = 5

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')


        qs = Abrigo.objects.annotate(qtd_voluntarios=Count('voluntario'))


        if buscar:
            qs = qs.filter(endereco__icontains=buscar)

        return qs


class AbrigoAddView(SuccessMessageMixin, CreateView):
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo cadastrado com sucesso'


class AbrigoUpdateView(SuccessMessageMixin, UpdateView):
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo atualizado com sucesso'


class AbrigoDeleteView(SuccessMessageMixin, DeleteView):
    model = Abrigo
    template_name = 'abrigo_apagar.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo deletado com sucesso'



