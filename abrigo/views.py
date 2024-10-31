from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin

from .forms import AbrigoModelForm
from .models import Abrigo

class AbrigosView(ListView):
    model = Abrigo
    template_name = 'abrigos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(AbrigosView, self).get_queryset()

        if buscar:
            return qs.filter(endereco__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            messages.info(self.request, 'Não existem abrigos cadastrados')
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


# VoluntarioAbrigoInLine = inlineformset_factory(
#     Abrigo,
#     VoluntariosAbrigo,
#     fk_name='abrigo',  # Define a chave estrangeira correta
#     fields=('voluntario', 'quantidade_horas'),
#     extra=1,
#     can_delete=True
# )
#
# class AbrigoInLineEditView(TemplateResponseMixin, View):
#     template_name = 'abrigo_form_inline.html'
#
#     def get_formset(self, data=None):
#         return VoluntarioAbrigoInLine(instance=self.abrigo, data=data)
#
#     def dispatch(self, request, pk):
#         self.abrigo = get_object_or_404(Abrigo, id=pk)
#         return super().dispatch(request, pk)
#
#     def get(self, request, *args, **kwargs):
#         formset = self.get_formset()
#         return self.render_to_response({'abrigo': self.abrigo, 'formset': formset})
#
#     def post(self, request, *args, **kwargs):
#         formset = self.get_formset(data=request.POST)
#         if formset.is_valid():
#             formset.save()
#             return redirect('abrigos')  # Redireciona para a lista de abrigos após salvar
#         return self.render_to_response({'abrigo': self.abrigo, 'formset': formset})
